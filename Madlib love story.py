 #madlib love story by Rita
print("Welcome to Rita's Madlib love story game!")
print("Let's create a funny love story\n")

name1=input("Enter boy's name:").lower()
name2=input("Enter girl's name:").lower()
place=input("Enter a romantic place:").lower()
verb1=input("Enter an action verb(ending with -ing):").lower()
noun1=input("Enter a cute object:").lower()
adjective1=input("Enter a sweet adjective:").lower()
verb2=input("Enter a fun activity verb:").lower()
food=input("Enter a food:").lower()
emotion=input("Enter an emotion:").lower()
gift=input("Enter a special gift:").lower()

# The story template
Story= f"""Once upon a time. There was a boy named {name1} who fell in love with a girl
named {name2}.
They first met at a magical place called {place}.While both were {verb1} near a giant{noun1}
From that moment,they knew it was love at first sight.
{name1} thought {name2} was the most {adjective1} person ever.
They started going on fun dates together, like {verb2} in the park and sharing delicious {food}
. Every time they met, they felt so much {emotion} inside their hearts.
On a very special day, {name1} gave {name2} a surprise gift - a {gift} - and said,
"will you be mine forever?"
And of course, {name2} said "YES!!!!"
From that day on, their love story became the most beautiful tale in {place}.

THE END"""

print("Here is your love story Madlib\n:")
print(Story)

