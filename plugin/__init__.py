# -*- coding: utf-8 -*-
from __future__ import print_function
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from os import environ as os_environ
import gettext

def localeInit():
	gettext.bindtextdomain("SetPicon", resolveFilename(SCOPE_PLUGINS, "Extensions/SetPicon/locale"))

def _(txt):
	t = gettext.dgettext("SetPicon", txt)
	if t == txt:
		print("[SetPicon] fallback to default translation for", txt)
		t = gettext.gettext(txt)
	return t

localeInit()
language.addCallback(localeInit)
