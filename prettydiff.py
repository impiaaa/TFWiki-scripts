statusRe = re.compile(r'^(\w)\s+\"?(.[^\"]+)\"?')
statusReRenamed = re.compile(r'^R\s+\"?(.[^\"]+)\"?\s+->\s+\"?(.[^\"]+)\"?')
			filename = newname
				if 'new file mode 100644' not in diff:
					contents = u(re.search(textFileRe, diff).group(3).encode('utf-8')).strip()
				else:
					contents = u''
		subPageName = u'Template:PatchDiff/' + patchName + u'/' + f['name'].replace("{", "(")
			page = wikitools.page.Page(wiki, subPageName)
					page.edit(finalText, summary=u'Diff of file "' + f['name'] + u'" for patch [[:' + patchName + u']].', minor=True, bot=True, skipmd5=True, timeout=60)
					page.setPageInfo()
					success = page.exists
				page.edit(u'<div class="diff-file">File too large to diff</div>', summary=u'Diff of file "' + f['name'] + u'" for patch [[:' + patchName + u']].', minor=True, bot=True, skipmd5=True)
	page = wikitools.page.Page(wiki, u'Template:PatchDiff/' + patchName)
			page.edit(patchDiff, summary=u'Diff of patch [[:' + patchName + u']].', minor=True, bot=True)
			page.setPageInfo()
			success = page.exists