''' Questions from Chatgpt for Practice'''


x = "5"  
y = 2  
z = x * y  
print(z) 

'''ab ek string ("5") aur ek integer (2) ko multiply karte ho, to string repeat hoti hai!
Output yeh hoga:

55

Error tab aata, agar tum string ko + ya / jaisa operator ke saath combine karte (jo allowed nahi hai).'''


a = 0.1 + 0.2  
print(a == 0.3)

'''Explanation:

    Python mein floating-point numbers exactly store nahi hote due to limitations of binary representation.
    0.1 aur 0.2 ka sum mathematically 0.3 hona chahiye, lekin Python mein yeh slightly off hota hai.
        0.1 + 0.2 actually 0.30000000000000004 banta hai.
    Jab a == 0.3 compare karte ho, to yeh False return karta hai kyunki a exactly 0.3 nahi hai.

Key Concept:
Floating-point arithmetic computers mein exact nahi hota. Isliye precision issues hote hain.

Tum is issue ko round() ka use karke fix kar sakte ho:

print(round(a, 1) == 0.3)  # Output: True'''


a = True + False + 5
print(a)

'''Explanation:

    Boolean as Numbers:
    Python mein, True aur False actually integers ke equivalent hote hain:
        True ki value hoti hai 1.
        False ki value hoti hai 0.

    Calculation:
        True + False + 5 ka matlab hai:
        1 + 0 + 5 = 6.

    No Error:
        Boolean values directly integers ke saath add ho sakte hain, kyunki Python internally unhein numbers treat karta hai.'''
        
x = "3" + "4"
y = 3 + 4
print(x, y)

'''Explanation:

    String concatenation ("3" + "4"):
        Pehle do strings ko add kiya ja raha hai, yani "3" aur "4".
        Iska result hoga:

    "34"

Adding Integer ("34" + 3):

    Ab tum string "34" ko integer 3 ke saath add karne ki koshish kar rahe ho.
    Python mein string aur integer ko directly add karna galat hai, kyunki incompatible types hain. Isliye yeh error dega.

Error Explanation:

    Agar tum yeh code run karoge, to Python ek TypeError throw karega.
    Error message hoga:

TypeError: can only concatenate str (not "int") to str'''

x = None
print(type(x))

'''x = None:

    None ek special constant hai jo "no value" ya "null" ko represent karta hai.
    Jab koi variable kisi value ko explicitly None assign kiya jata hai, iska matlab hai ke is variable ko koi value nahi di gayi, ya phir is variable ko intentionally empty (null) chhoda gaya hai.

type(x):

    type() function se hum kisi bhi variable ka data type jaan sakte hain.

    Jab tum None ko x mein assign karte ho, toh type(x) ka result <class 'NoneType'> hoga.

    NoneType Python ka ek special data type hai, jo sirf None value ke liye use hota hai.

Output:

<class 'NoneType'>'''


x = 5
y = 2.0
print(x + y)

'''
Explanation:

    x = 5:
    x ek integer hai.

    y = 2.0:
    y ek float hai.

    Addition of Integer and Float:
    Jab tum integer aur float ko add karte ho, toh Python automatically integer ko float mein convert kar leta hai, taki addition properly ho sake.
        5 + 2.0 ka result hoga 7.0, kyunki integer ko float mein convert kiya gaya.

    Output:

7.0'''

a = "5" * 2
b = 5 * "2"
print(a, b)

'''Explanation:

    a = "5" * 2:
        Yahan "5" ek string hai aur hum is string ko 2 se multiply kar rahe hain.
        Jab string ko ek number se multiply kiya jata hai, toh woh string utni baar repeat ho jati hai.
        Output for a:

    "55"  # "5" repeated 2 times

b = 5 * "2":

    Yahan 5 ek integer hai aur "2" ek string hai.
    Python mein integer aur string ka multiplication valid hota hai, jisme string utni baar repeat hoti hai jitni baar integer diya gaya ho.
    Output for b:

    "22222"  # "2" repeated 5 times

Final output:

"55" "22222"'''


x = 10
y = 4
z = x / y
print(z)

'''
Explanation:

    x = 10:
    x ek integer hai, jiska value 10 hai.

    y = 4:
    y bhi ek integer hai, jiska value 4 hai.

    Division Operation:
    Jab tum integer division karte ho, Python mein / operator ka use always float division ke liye hota hai, chahe tum dono operands integers ho. Isliye, x / y ka result float hoga.
        10 / 4 ka result 2.5 hoga, kyunki floating-point division ki wajah se result decimal value mein aayega.

    Output:

    2.5

Key Concept:

    Python mein, / operator always float result deta hai, even if both numbers are integers.'''

x = 3 + 4j
y = 1 + 2j
print(x + y)

'''Explanation:

    Complex Numbers in Python:
        x = 3 + 4j:
        Yahan, x ek complex number hai, jisme 3 real part hai aur 4j imaginary part hai. Python mein imaginary number ko j ke saath likha jata hai.
        y = 1 + 2j:
        Yahan bhi y ek complex number hai, jisme 1 real part hai aur 2j imaginary part hai.

    Addition of Complex Numbers:
        Jab tum do complex numbers ko add karte ho, toh unke real parts ko alag se aur imaginary parts ko alag se add kiya jata hai:
            Real part: 3 + 1 = 4
            Imaginary part: 4j + 2j = 6j
        Isliye, x + y ka result 4 + 6j hoga.

    Output:

    (4+6j)

Key Concept:

    Complex numbers ko Python mein a + bj format mein represent kiya jata hai, jahan a real part hai aur b imaginary part hai.
    Jab complex numbers ko add ya subtract kiya jata hai, to real aur imaginary parts ko separately add ya subtract kiya jata hai.'''


a = True + 2
b = False + 3
print(a, b)

'''Explanation:

    a = True + 2:
        True ko Python mein 1 ke equivalent treat kiya jata hai.
        Jab tum True ko 2 ke saath add karte ho, toh 1 + 2 = 3.
        Isliye a ka value 3 hoga.

    b = False + 3:
        False ko Python mein 0 ke equivalent treat kiya jata hai.
        Jab tum False ko 3 ke saath add karte ho, toh 0 + 3 = 3.
        Isliye b ka value 3 hoga.

    Output: 3 3'''
    
    
a = 4.5
b = 2
c = a // b
print(c)

'''a // b:
        Yahan, hum // operator use kar rahe hain, jo floor division ka kaam karta hai. Floor division ka matlab hai division ke result ka integer part lena, yaani decimal ko ignore karna.
        Jab hum 4.5 ko 2 se divide karte hain, toh normally result 2.25 aata hai. Lekin // use karne se decimal part ko hata diya jata hai, aur integer part 2 milta hai.

    Note: Floor division hamesha integer result deta hai, chahe aap float aur integer ke beech division kar rahe ho.

    Output:
        Is liye, c ka value 2 hoga, aur print(c) ka output 2 hoga.

Key Points:

    // operator: Yeh operator floor division ke liye use hota hai, jisme division ka result decimal part ke bina diya jata hai.
    Agar aap integer aur float ko divide kar rahe hain, to floor division result hamesha integer hi hoga (decimal part ko ignore karke).'''
    
    
