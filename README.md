# qiushibaike-crawler
Interpreter Version: `python2.7`<br/>
Dependencies: `urllib2`, `re`<br/>
## Instruction
In command line, input `python qiubai-crawler.py` or `python main.py'<br>
## Demo
![image](https://github.com/xx-zhou16/qiushibaike-crawler/blob/master/images/1.png)
## Progress
#### code change
`(.*?)`<br/>
`response.read().decode('utf-8')`</br>
#### html escape characters
`target = re.search(r'<span>(.*?)</span>', item[1], re.S)`<br/>
`replaceBR = re.compile('<br/>')`<br>
`text = re.sub(replaceBR, "\n", target.group(1).strip())`<br/>
`replaceQUOT = re.compile('&quot')`<br/>
`text = re.sub(replaceQUOT, '"', text)`<br/>
## Problems
I can't handle `gbk` coding problems <br/>
www.qiushibaike.com updates sometimes, and when it updates, this program doesn't work <br/>
