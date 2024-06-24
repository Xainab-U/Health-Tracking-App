'''This module will help you to know your overall fitness'''

#BMI
def bmi(weight,height):
    bmi1 = float( weight/height**2)
    if bmi1 <16:
            r=("BMI="+" "+str(round(bmi1,2))+" "+"Severely UnderWeight")
    elif bmi1 >=16 and bmi1 <17:
            r=("BMI="+" "+str(round(bmi1,2))+"  "+"Underweight")
    elif bmi1 >=17 and bmi1 <18.5:
            r=("BMI="+" "+str(round(bmi1,2))+"  "+"Slightly UnderWeight")
    elif bmi1 >= 18.5 and bmi1 <=25.0:
            r=("BMI="+" "+str(round(bmi1,2))+"  "+"Normal weight")
    elif bmi1 >25.0 and bmi1 <30:
            r=("BMI="+" "+str(round(bmi1,2))+"  "+"Slightly Overweight")
    elif bmi1 >=30.0 and bmi1 <35:
            r=("BMI="+" "+str(round(bmi1,2))+"  "+"Overweight")
    else:
            r=("BMI="+" "+str(round(bmi1,2))+"  "+"Severely Overweight")
    return r



#BP
def bp(sys,dia):
    if sys<90 and dia<=60:
        r=("LOW BLOOD PRESSURE")
    elif (sys>=90 and sys<120) and (dia>60 and dia<80):
        r=("NORMAL BLOOD PRESSURE")
    elif (sys>=120 and sys<130) and (dia>=80 and dia<90):
        r=("ELEVATED BLOOD PRESSURE")
    elif (sys>=130 and sys<140) and (dia>=90 and dia<100):
        r=("HIGH BLOOD PRESSURE-HYPERTENSION")
    elif sys>=140 and dia>100:
        r=("HYPERTENSIVE CRISIS")
    else:
        r=("invalid values")

    return r


#CALORIES BURNT
def calorie(time):
    return ("You lost"+" "+str(round(time * 3.4,3))+" "+"calories.")


#HEART BEAT
def heart(a,b):#a=age;b=bpm
    if a<0.5:
        if b>=160:
            r="Heart beat is high."
        elif b<160 and b>100:
            r="Heart in good condition."
        else:
            r="Heart beat is low."
    elif a<1:
        if b>=140:
            r="Heart beat is high."
        elif b<140 and b>80:
            r="Heart in good condition."
        else:
            r="Heart beat is low."
    elif a<4:
        if b>=130:
            r="Heart beat is high."
        elif b<130 and b>80:
            r="Heart in good condition."
        else:
            r="Heart beat is low."
    elif a<6:
        if b>=120:
            r="Heart beat is high."
        elif b<120 and b>80:
            r="Heart beat in good."
        else:
            r="Heart beat is low."
    elif a<11:
        if b>=110:
            r="Heart beat is high."
        elif b<110 and b>70:
            r="Heart beat  is good."
        else:
            r="Heart beat is low."
    elif a<15:
        if b>=105:
            r="Heart beat is high."
        elif b<105 and b>60:
            r="Heart beat is good."
        else:
            r="Heart beat is low."
    else:
        if b>=100:
            r="Heart beat is high."
        elif b<100 and b>60:
            r="Heart beat is good."
        else:
            r="Heart beat is low."
    return r


#PULSE RATE
def pulse(age,pulse4):
    
    max_heart_rate= int(220-age)
    min_target = (65/100)*max_heart_rate
    max_target =(85/100)*max_heart_rate

    if pulse4 >=min_target and pulse4 <= max_target:
        r=("You are exercising well keep going!!")
    elif pulse4 >max_target and pulse4 <= max_heart_rate:
        r=("Slow down your target heart rate should be in between"+" "+str(min_target)+" "+"and"+" "+str(max_target))
    elif  pulse4 > max_heart_rate:
        r=("Stop your target heart rate should be in between"+" "+str(min_target)+" "+"and"+" "+str(max_target))
    elif pulse4 < min_target :
        r=(" Exercise harder your target heart rate should be in between"+" "+str(min_target)+" "+"and"+" "+str(max_target))

    return r


#S U G A R
def random(r):#random    
    if (r>=60 and r<80):
        a=("low Blood Sugar level-Hypoglycemia")
    elif (r>=80 and r<=140):
        a=("Normal Blood sugar level")
    elif (r>140 and r<=160):
        a=("Boderline Blood sugar level ")
    elif (r>160):
        a=("high Blood Sugar level-Hyperglycemia")
    else:
        a=("enter valid values")
    return a


def fasting(f):#fasting
    if (f>40 and f<80):
        a=("low Blood Sugar level-Hypoglycemia ")
    elif (f>=80 and f<=110):
        a=("Normal Blood sugar level ")
    elif (f>110 and f<=125):
        a=("Boderline Blood sugar level ")
    elif (f>125):
        a=("high Blood Sugar level-Hyperglycemia ")
    else:
        a=("enter valid values")
    return a


def p_p(p):#post-prandial
    if (p>=70 and p<140 ):
        c=("low Blood Sugar level-Hypoglycemia")
    elif (p>=140 and p<=160):
        c=("Normal Blood sugar level")
    elif (p>160 and p<200):
        c=("Boderline Blood Sugar level")
    elif (p>=200):
        c=("high Blood Sugar level-Hyperglycemia")
    else:
        c=("enter valid values")
    return c


def Hb1Ac(h):#HbA1c    
    if (h>3 and h<=4):
        d=("low Blood Sugar level-Hypoglycemia")
    elif (h>4 and h<=6):
        d=("Normal Blood sugar level")
    elif (h>6 and h<=8):
        d=("Boaderline Blood sugar level ")
    elif (h>8 and h<=14):
        d=("high Blood Sugar level-Hyperglycemia")
    else:
        d=("enter valid values")
    return d
