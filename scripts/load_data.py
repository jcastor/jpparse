django_project_home="/home/jcastor/django/myproject/"
import sys,os
sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

from jpparse.models import Method,Class,Variable,GlobalVariable,CodeSegment
import csv,re

classpattern = r'^(C;)'
gvpattern = r'^(GV;)'
methodpattern = r'^(M;)'
varpattern = r'^(V;)'
sigpattern = r'^(Signature;)'
codepattern = r'^(Code;)'

classregex = re.compile(classpattern)
gvregex = re.compile(gvpattern)
methodregex = re.compile(methodpattern)
varregex = re.compile(varpattern)
sigregex = re.compile(sigpattern)
coderegex = re.compile(codepattern)


csv_filepathname=sys.argv[1]
f = open(csv_filepathname)
ingv = 0
inmethod = 0
for row in f:
	row = row.rstrip('\n')
	findClass = classregex.match(row)
	findGV = gvregex.match(row)
	findMethod = methodregex.match(row)
	findVar = varregex.match(row)
	findSig = sigregex.match(row)
	findCode = coderegex.match(row)
	if findClass:
		currentclass = row.split('C;')[1]
		newclass = Class()
		newclass.name = currentclass
		newclass.save()
		ingv = 0
		inmethod = 0
	if findGV:
		currentgv = row.split('GV;')[1]
		newgv = GlobalVariable()
		newgv.name = currentgv
		newgv.classowner = newclass
		newgv.save()
		ingv = 1
		inmethod = 0
	if findMethod:
		currentmethod = row.split('M;')[1]
		newmethod = Method()
		newmethod.name = currentmethod
		newmethod.save()
		newclass.methods.add(newmethod)
		newclass.save()
		inmethod = 1
		ingv = 0
	if findVar:
		currentvar = row.split(';')[1]
		newvar = Variable()
		newvar.name = currentvar
		newvar.method = newmethod
		newvar.signature = row.split(';')[2]
		newvar.save()
	if findSig:
		currentsig = row.split('Signature;')[1]
		if ingv:
			newgv.signature = currentsig
			newgv.save()	
		if inmethod:
			newmethod.signature = currentsig
			newmethod.save()
	if findCode:
		currentcode = row.split('Code;')[1]
		codearray = re.findall(r'\d+', currentcode)
		newcode = CodeSegment()
		try:
			newcode.stack = int(codearray[0])
		except IndexError:
			newcode.stack = 0
		try:
			newcode.local = int(codearray[1])
		except IndexError:
			newcode.local = 0
		try:
			newcode.args_size = int(codearray[2])
		except IndexError:
			newcode.args_size = 0
		try:
			newcode.length = int(codearray[3])
		except IndexError:
			newcode.length = 0
		newcode.method = newmethod
		newcode.save()
print "finished" + sys.argv[1]
f.close()
