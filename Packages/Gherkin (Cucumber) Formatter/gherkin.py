import os
import re

from StringIO import StringIO


class Tokens(object):
  TEXT = 1
  GROUP = 2
  INDENT = 4
  NEWLINE = 8


class GherkinParser(object):

  def __init__(self, gherkin_text):
    self._gherkin_text = StringIO(gherkin_text)
    self._tokens = []
    self._group = []
    self._group_indent = 0

  def parse(self):
    example_re = re.compile(r'\s*\|[^|]+\|\s*')

    for line in self._gherkin_text.readlines():

      if example_re.match(line):
        self._collect_group_item(line)

      else:
        self._store_and_reset_group()
        line = self._strip_and_store_indent(line)
        self._add_text_token(line)

    self._finish()

    return self._tokens

  def _collect_group_item(self, line):
    if len(self._group) == 0:
      indent = self._extract_indent(line)
      if indent:
        self._group_indent = len(indent)

    elements = [item.strip() for item in line.split('|')[1:-1]]
    self._group.append(elements)

  def _store_and_reset_group(self):
    if len(self._group) > 0:
      self._append_token(Tokens.GROUP, self._group, {'indent': self._group_indent})
      self._group = []
      self._group_indent = 0

  def _strip_and_store_indent(self, line):
    indent = self._extract_indent(line)

    if indent:
      self._append_token(Tokens.INDENT, indent)
      return line.lstrip()

    return line

  def _add_text_token(self, text):
    if len(text):
      self._append_token(Tokens.TEXT, text.rstrip())

    # TODO: detect exact line seperator used (for non Unix systems)
    self._append_token(Tokens.NEWLINE, '\n')

  def _extract_indent(self, text):
    match = re.compile(r'(\ +)').match(text)
    return match.groups()[0] if match else None

  def _append_token(self, type, data, meta=None):
    self._tokens.append((type, data, meta or {}))

  def _finish(self):
    self._store_and_reset_group()


class GherkinFormatter(object):

  def __init__(self):
    self._result = StringIO()

  def format(self, parsed):
    for token_type, token, meta_data in parsed:

      if token_type in [Tokens.TEXT, Tokens.INDENT, Tokens.NEWLINE]:
        self._emit(token)

      elif token_type == Tokens.GROUP:
        self._format_group(token, meta_data['indent'])

      else:
        raise Exception('unsupported token type %s' % token_type)

    result = self._result.getvalue()
    self._result.close()

    return result

  def _format_group(self, group, indent):
    widths = self._determine_column_widths(group)

    for line in group:
      buf = StringIO()
      buf.write(' ' * indent)
      buf.write('|')

      for idx, col in enumerate(line):
        width = widths[idx]
        padding = width - len(col)
        buf.write(' ')
        buf.write(col)
        buf.write(' ' * padding)
        buf.write(' |')

      buf.write('\n')
      self._emit(buf.getvalue())
      buf.close()

  def _determine_column_widths(self, group):
    widths = []

    for i in range(len(group[0])):
      width = 0
      for j in range(len(group)):
        width = max(len(group[j][i]), width)
      widths.append(width)

    return widths

  def _emit(self, text):
    self._result.write(text)
