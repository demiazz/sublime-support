# Sublime modelines - https://github.com/SublimeText/Modelines
# sublime: translate_tabs_to_spaces false; rulers [100,120]

import sublime
import sublime_plugin
import gscommon as gs
import mg9
import gspatch

DOMAIN = 'GsFmt'

class GsFmtCommand(sublime_plugin.TextCommand):
	def is_enabled(self):
		return gs.setting('fmt_enabled', False) is True and gs.is_go_source_view(self.view)

	def run(self, edit):
		vsize = self.view.size()
		src = self.view.substr(sublime.Region(0, vsize))
		if not src.strip():
			return

		src, err = mg9.fmt(self.view.file_name(), src)
		if err:
			gs.println(DOMAIN, "cannot fmt file. error: `%s'" % err)
			return

		if not src.strip():
			gs.println(DOMAIN, "cannot fmt file. it appears to be empty")
			return

		_, err = gspatch.merge(self.view, vsize, src)
		if err:
			msg = 'PANIC: Cannot fmt file. Check your source for errors (and maybe undo any changes).'
			sublime.error_message("%s: %s: Merge failure: `%s'" % (DOMAIN, msg, err))
