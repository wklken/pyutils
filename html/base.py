#!/usr/bin/env python
# encoding: utf-8


#source: https://github.com/bottlepy/bottle/blob/master/bottle.py
def html_escape(string):
    """ Escape HTML special characters ``&<>`` and quotes ``'"``. """
    return string.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')\
                 .replace('"', '&quot;').replace("'", '&#039;')


#source: https://github.com/bottlepy/bottle/blob/master/bottle.py
def html_quote(string):
    """ Escape and quote a string to be used as an HTTP attribute."""
    return '"%s"' % html_escape(string).replace('\n', '&#10;')\
                    .replace('\r', '&#13;').replace('\t', '&#9;')


# source: django
def htmlquote(text):
    r"""
    Encodes `text` for raw use in HTML.

        >>> htmlquote(u"<'&\">")
        u'&lt;&#39;&amp;&quot;&gt;'
    """
    text = text.replace(u"&", u"&amp;")  # Must be done first!
    text = text.replace(u"<", u"&lt;")
    text = text.replace(u">", u"&gt;")
    text = text.replace(u"'", u"&#39;")
    text = text.replace(u'"', u"&quot;")
    return text


# source: django
def htmlunquote(text):
    r"""
    Decodes `text` that's HTML quoted.

        >>> htmlunquote(u'&lt;&#39;&amp;&quot;&gt;')
        u'<\'&">'
    """
    text = text.replace(u"&quot;", u'"')
    text = text.replace(u"&#39;", u"'")
    text = text.replace(u"&gt;", u">")
    text = text.replace(u"&lt;", u"<")
    text = text.replace(u"&amp;", u"&")  # Must be done last!
    return text
