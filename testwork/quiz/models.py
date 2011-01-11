from django.db import models

# Create your models here.

class subjectsQuiz(models.Model):
	title = models.CharField(max_length = 100, null = False)
	def __unicode__(self):
		return self.title

class chaptersQuiz(models.Model):
	title = models.CharField(max_length = 100, null = False)
	def __unicode__(self):
		return self.title

class casesQuiz(models.Model):
	title = models.CharField(max_length = 100, null = False)
	def __unicode__(self):
		return '%s %s' % (self.id, self.title)

class titlesQuiz(models.Model):
	title = models.CharField(max_length = 100, null = False)
	def __unicode__(self):
		return self.title

class tagsQuiz(models.Model):
	title = models.CharField(max_length = 100, null = False)
	def __unicode__(self):
		return self.title

ANSWER_CHOICES = (
				('1', '1'),
				('2', '2'),
				('3', '3'),
				('4', '4'),
				('5', '5'),
				)

class quizzes(models.Model):
	id = 0
	subject = models.ForeignKey(subjectsQuiz)
	chapter = models.ForeignKey(chaptersQuiz)
	case = models.ForeignKey(casesQuiz)
	titleQuiz = models.ForeignKey(titlesQuiz)
	textQuiz = models.TextField(blank = True)
	firstAnswer = models.CharField(max_length = 100, null = False)
	secondAnswer = models.CharField(max_length = 100, null = False)
	thirdAnswer = models.CharField(max_length = 100, null = False)
	fourthAnswer = models.CharField(max_length = 100, null = False)
	fifthAnswer = models.CharField(max_length = 100, blank = True)
	answerQuiz = models.CharField(max_length = 1, choices = ANSWER_CHOICES)
	tagQuiz = models.ManyToManyField(tagsQuiz)
	hintQuiz = models.TextField(blank = True)
	solutionQuiz = models.TextField(blank = True)
	cTime = models.DateTimeField(auto_now_add = True)
	mTime = models.DateTimeField(auto_now = True)
	is_public = models.BooleanField()
	is_right = models.BooleanField()
	allAnswer = models.TextField(blank = True)
	scoreAnswer = models.CharField(max_length = 100, blank = True)



	def __unicode__(self):
		return u'%s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.case, self.textQuiz, self.firstAnswer, self.secondAnswer,
					self.thirdAnswer, self.fourthAnswer, self.fifthAnswer,
					self.answerQuiz, self.hintQuiz, self.solutionQuiz,)

'''
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)
		
'''
