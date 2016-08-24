#!/usr/bin/python
 
import gettext
 
APP = "hello"
 
gettext.textdomain ( APP )
gettext.bindtextdomain ( APP, "./mo" )
 
_ = gettext.gettext
 
print _("hello, world!")

print _("goodbye")
