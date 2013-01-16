package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
	"sync"
	"time"
)

var (
	byeLck            = sync.Mutex{}
	byeFuncs *byeFunc = nil
	numbers           = &counter{}
	logger            = log.New(os.Stderr, "margo: ", log.Ldate|log.Ltime|log.Lshortfile)
)

type counter struct {
	lck sync.Mutex
	n   uint64
}

func (c *counter) next() uint64 {
	c.lck.Lock()
	defer c.lck.Unlock()
	c.n += 1
	return c.n
}

func (c *counter) nextString() string {
	c.lck.Lock()
	defer c.lck.Unlock()
	c.n += 1
	return fmt.Sprint(c.n)
}

type byeFunc struct {
	prev *byeFunc
	f    func()
}

func byeDefer(f func()) {
	byeLck.Lock()
	defer byeLck.Unlock()
	byeFuncs = &byeFunc{
		prev: byeFuncs,
		f:    f,
	}
}

func main() {
	do := "-"
	poll := 0
	wait := false
	dump_env := false
	flag.BoolVar(&dump_env, "env", dump_env, "if true, dump all environment variables as a json map to stdout and exit")
	flag.BoolVar(&wait, "wait", wait, "Whether or not to wait for outstanding requests (which may be hanging forever) when exiting")
	flag.IntVar(&poll, "poll", poll, "If N is greater than zero, send a response every N seconds. The token will be `margo.poll`")
	flag.StringVar(&do, "do", "-", "Process the specified operations(lines) operation and exit. `-` means operate as normal")
	flag.Parse()

	if dump_env {
		m := defaultEnv()
		for _, s := range os.Environ() {
			p := strings.SplitN(s, "=", 2)
			if len(p) == 2 {
				m[p[0]] = p[1]
			} else {
				m[p[0]] = ""
			}
		}
		json.NewEncoder(os.Stdout).Encode(m)
		os.Exit(0)
	}

	var in io.Reader = os.Stdin
	doCall := do != "-"
	if doCall {
		b64 := "base64:"
		if strings.HasPrefix(do, b64) {
			s, _ := base64.StdEncoding.DecodeString(do[len(b64):])
			in = bytes.NewReader(s)
		} else {
			in = strings.NewReader(do)
		}
	}

	broker := NewBroker(in, os.Stdout)
	if poll > 0 {
		pollSeconds := time.Second * time.Duration(poll)
		pollCounter := &counter{}
		go func() {
			for {
				time.Sleep(pollSeconds)
				broker.SendNoLog(Response{
					Token: "margo.poll",
					Data: M{
						"time": time.Now().String(),
						"seq":  pollCounter.nextString(),
					},
				})
			}
		}()
	}
	broker.Loop(!doCall)

	if wait || doCall {
		broker.Wg.Wait()
	}

	byeLck.Lock()
	defer byeLck.Unlock() // keep this here for the sake of code correctness
	for b := byeFuncs; b != nil; b = b.prev {
		func() {
			defer func() {
				err := recover()
				if err != nil {
					logger.Println("PANIC defer:", err)
				}
			}()

			b.f()
		}()
	}

	os.Exit(0)
}
