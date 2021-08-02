import time #ספרייה זמן
import turtle #ספרייה מערכת צירים של מערכת שמש
wn=turtle.Screen()
wn.bgcolor("black") #שינוי רקע שחור
wn.setup(width=500 , height=500) #שינוי גודל של המסך
wn.title("Simple Analog Clock by Gal Oz")  #כותרת
wn.tracer(0)   #כיבוי האנמציה תוך כדי שהוא מצייר אותה

#עט שרטוט
pen=turtle.Turtle()
pen.hideturtle() #הסתרת עט שרטוט
pen.speed(0)   #מהירות השרטוט
pen.pensize(3) #גודל העט

#פונקציית שרטוט שעון ע"י העט שיצרנו (הגדרת פונקציה)
def draw_clocke(h, m, s, pen):
    #ציור פרצוף של השעון
    pen.up()  #לא לצייר קו
    pen.goto(0,210)   #מרכוז ראשית הצירים בשעון
    pen.setheading(180)  #זווית סיבוב של המחוג
    pen.color("green")   #צביעת המעגל בצבע ירוק
    pen.pendown()
    pen.circle(210, extent=None, steps=None)  #קביעת רדיוס המעגל
  
    #ציור קווי שעות
    pen.penup()   #להחזיר את העט למרכז
    pen.goto(0,0) #מרכוזר ראשית צירים של המחוג
    pen.setheading(90)   #זווית סיבוב של המחוג
    
    for _ in range(12):    #טווח של 12 שעות- יצירת קווים של השעות בשעון
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30) # טווח שינוי שעה ב 30 מעלות על 12 שעות מה שיוצר 360
    
    #ציור מחוג שעות
    pen.penup()  
    pen.goto(0,0) #מרכוז מחוג למרכז
    pen.color("white") #צביעת המחוג בצבע לבן
    pen.setheading(90)   # הגדרת זווית התחלתית
    angle= (h/12) *360 # משווה של כל כמה זמן המחוג יזוז וכמה
    pen.rt(angle)
    pen.pendown()
    pen.fd(90)   #אורך המחוג

#ציור מחוג דקות
    pen.penup()  
    pen.goto(0,0) #מרכוז מחוג למרכז
    pen.color("blue") #צביעת המחוג בצבע כחול
    pen.setheading(90)   # הגדרת זווית התחלתית
    angle= (m/60) *360 # משווה של כל כמה זמן המחוג יזוז וכמה
    pen.rt(angle)
    pen.pendown()
    pen.fd(130)   #אורך המחוג

#ציור מחוג שניות
    pen.penup()  
    pen.goto(0,0) #מרכוז מחוג למרכז
    pen.color("gold") #צביעת המחוג בצבע זהב
    pen.setheading(90)   # הגדרת זווית התחלתית
    angle= (s/60) *360 # משווה של כל כמה זמן המחוג יזוז וכמה
    pen.rt(angle)
    pen.pendown()
    pen.fd(170)   #אורך המחוג

#הגדרת שעון בזמן אמת
while True:
    h= int(time.strftime("%I"))   #התמרה של הזמן שלנו מדיגיטלי לאנלוגי
    m= int(time.strftime("%M"))   #התמרה של הזמן שלנו מדיגיטלי לאנלוגי
    s= int(time.strftime("%S"))   #התמרה של הזמן שלנו מדיגיטלי לאנלוגי

    draw_clocke(h,m,s,pen)    #פקודה לצייר את כל ההגדרה של השעון
    wn.update()   #הוצאה מתוך הזיכרון של כמה מה שהתוכנית ציירה
    time.sleep(1)
    pen.clear()   #לנקות את השעות אחרי כל עידכון של זמן אמת

wn.mainloop() #פונקציה שגורמת לחלון לא להיסגר ישר אחרי שנריץ את התוכנית
