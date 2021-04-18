def tree(x,y):
	#import
	import math
	import turtle
	#variables
	tri_size=400
	angle=120
	next_div=2
	col1='#00'
	col2='9'
	col3='700'
	#method
	def triangle(turtle,lenght,col):
		"""Drawing triangle method"""
		t.color(col)
		t.lt(60)
		for x in range(3):
			turtle.fd(lenght)
			turtle.lt(120)
		t.rt(60)
	def col_join(col1,col2,col3):
		return col1+col2+col3
	def col_change(col2):
		col2=int(col2)
		col2-=1
		return str(col2)
	def col_change2(col2):
		col2=int(col2)
		col2+=1
		return str(col2)
	def home_set(t):
		pos_1x=t.xcor()
		pos_1y=t.ycor()
		return pos_1x,pos_1y
	def home(t,pos_1x,pos_1y):
		t.goto(pos_1x,pos_1y)
		t.rt(90)
	#setup
	t=turtle
	t.bgcolor('darkblue')
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color(str(col_join(col1,col2,col3)))
	t.pensize(10)
	pos_1x,pos_1y=home_set(t)
	t.speed(0)
	t.hideturtle()
	#start position
	t.penup()
	t.right(90)
	t.fd(173)
	t.pendown()
	t.lt(90)
	#### 1
	#triangle 1
	t.begin_fill()
	t.fd(tri_size/next_div)
	t.lt(angle)
	t.fd(tri_size)
	t.lt(angle)
	t.fd(tri_size)
	t.lt(angle)
	t.fd(tri_size/next_div)
	col2=col_change(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#### 2
	col2=col_change(col2)
	#triangle 2
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#### 3
	col2=col_change(col2)
	#change position
	t.penup()
	next_div*=2
	t.fd(tri_size/next_div)
	t.pendown()
	#triangle 3.1
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	pos1x=t.xcor()
	pos1y=t.ycor()
	#change position
	t.penup()
	t.lt(180)
	t.fd(2*tri_size/next_div)
	t.rt(180)
	t.pendown()
	#triangle 3.2
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	pos2x=t.xcor()
	pos2y=t.ycor()
	#change position
	t.penup()
	t.lt(90)
	home(t,pos_1x,pos_1y)
	t.pendown()
	#triangle 3.3
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#### 4.1
	col2=col_change(col2)
	#change position
	t.penup()
	next_div*=2
	t.fd(tri_size/next_div)
	t.pendown()
	#triangle 4.1.1
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#change position
	t.penup()
	t.lt(180)
	t.fd(2*tri_size/next_div)
	t.rt(180)
	t.pendown()
	#triangle 4.1.2
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#change position
	t.penup()
	t.fd(tri_size/next_div)
	t.lt(90)
	t.fd(86.60254037844386)
	t.rt(90)
	t.pendown()
	#triangle 4.1.3
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#### 4.2
	#change position
	t.penup()
	t.goto(pos1x,pos1y)
	t.fd(tri_size/next_div)
	t.pendown()
	#triangle 4.2.1
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#change position
	t.penup()
	t.lt(180)
	t.fd(2*tri_size/next_div)
	t.rt(180)
	t.pendown()
	#triangle 4.2.2
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#change position
	t.penup()
	t.fd(tri_size/next_div)
	t.lt(90)
	t.fd(86.60254037844386)
	t.rt(90)
	t.pendown()
	#triangle 4.2.3
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#### 4.3
	#change position
	t.penup()
	t.goto(pos2x,pos2y)
	t.fd(tri_size/next_div)
	t.pendown()
	#triangle 4.3.1
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	pos3x=t.xcor()
	pos3y=t.ycor()
	#change position
	t.penup()
	t.lt(180)
	t.fd(2*tri_size/next_div)
	t.rt(180)
	t.pendown()
	#triangle 4.3.2
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	col2=col_change(col2)
	#change position
	t.penup()
	t.fd(tri_size/next_div)
	t.lt(90)
	t.fd(86.60254037844386)
	t.rt(90)
	t.pendown()
	#triangle 4.3.3
	t.begin_fill()
	triangle(t,tri_size/next_div,str(col_join(col1,col2,col3)))
	col2=col_change2(col2)
	t.color(str(col_join(col1,col2,col3)))
	t.end_fill()
	####part two
	#change position
	t.penup()
	t.color('#804000')
	t.goto(pos3x,pos3y)
	t.pendown()
	#draw
	t.begin_fill()
	t.rt(90)
	t.fd(50)
	t.lt(90)
	t.fd(100)
	t.lt(90)
	t.fd(50)
	t.penup()
	t.lt(90)
	t.fd(100)
	t.color('#703000')
	t.end_fill()
	t.lt(180)
tree(0,0)
