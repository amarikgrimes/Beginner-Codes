#name: amari grimes
#date: 2/23/2022
#course: SCIS105
#section: 1
#title: lyrics analyzer advanced
#description: creating a program that counts the words in a song that the user choses from the menu

print("welcome to lyric analyzer!")
print("\n")
print(".............................................................")
print(" 1 - the other woman lyrics")
print(" 2 - spelman hymm lyrics")
print(".............................................................")
print("\n")
userInput = int(input("please choose lyrics from the menu!: "))
print("\n")

text = """
The other woman has time to manicure her nails
The other woman is perfect where her rival fails
And she's never seen with pin curls in her hair, anywhere
The other woman enchants her clothes with French perfume
The other woman keeps fresh-cut flowers in each room
There are never toys that's scattered everywhere
And when her old man comes to call
He finds her waiting like a lonesome queen
'Cause to be by her side
It's such a change from old routine
But the other woman will always cry herself to sleep
The other woman will never have his love to keep
And as the years go by, the other woman
Will spend her life alone
Alone
Alone
"""
  
text2 = """
Spelman, thy name we praise
Standards and honor raise,
We‟ll ever faithful be
Throughout eternity.
May peace with thee abide
And God forever guide
Thy heights supreme and true.
Blessings to you.

Through years of toil and pain
May thy dear walls remain
Beacons of heavenly light,
Undaunted by the fight;
And when life‟s race is won,
Thy noble work is done,
Oh God, forever bind
Our hearts to thine.
"""

if userInput == 1: 
  print(f"you chose 'the other woman by lana del rey!' here is your analysis and lyrics: \n {text}")
else:
  print(f"you chose 'the spelman hymm!' here are your lyrics: \n {text2} ")


    
