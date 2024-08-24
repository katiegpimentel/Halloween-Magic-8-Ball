# --------------------------------------------------------
#        Name: Katie Pimentel
#        Date Last worked on: October 1st, 2023
# ------------------------------------------------------
import random

#the responses that are randomly generated. I added some that has some of my humor. Some others are because this is from a witches perspective.
randomly_generated_answers = ['It is certain.', 'It is decidedly so.','Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 'As I see it yes.','Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply was hazy try again.', 'Ask again later, but I\'d rather you leave me alone.', 'Better not tell you now.', 'Concentrate and ask again. I know that is hard to ask of a human but try.', 'Don\'t count on it.', 'My reply is no.', 'My cauldron says no.', 'Outlook not so good.', 'Very doubtful.', 'Umm... anyways... ask again lol', 'I had to laugh... no.', "My cauldron says yes.", "lol no"]

#Halloween Themed because it's October. Witch themed really.
print ("""Welcome to the Witches Cauldron Ball... Ask us a question and we shall tell you the truth whether you like it or not. \n""")

#got this from (https://asciiart.website/index.php?art=holiday/halloween)
print ('          (    ')
print('            )  )')
print('       ______(____')
print('      (___________)')
print('      /           \\')
print('     /             \\')
print('    |               |')
print(' ____\             /____')
print("()____'.__     __.'____()")
print("     .'` .'```'. `-.")
print("    ().'`       `'.()")
print()



# I want to refer them by their name. also a little mean, but Halloween <3
your_name = input('What is your name, you mere mortal? ')

your_sentence = input('\nSo, {}. Ask your question, if you dare... '.format(your_name))

#i put all stop's bc some ppl don't wanna do all caps
#the loop so that they can keep on asking questions
while your_sentence != 'STOP' and your_sentence != 'stop' and your_sentence != 'Stop': 

#the Ellipsis bc I don't like how a comma looks. 
#used format to make it look nicer. 
#Made it so that they refer to them as their name and used random.choice to it could generate the answers randomly. 
  print ('{}... {}' .format(your_name, random.choice(randomly_generated_answers)))
  print() #whitespace <3
  your_sentence = input('Ask another question, if you are brave enough to do so. Say STOP if you do not have anymore questions: ') #have to input this if they have another question

#after they say stop, this will print out. I said Happy Halloween bc it's Halloween themed. Tis the season and all.
print() #whitespace <3
print ("""You made it out alive?🙄  Ugh, another pesky human on our streets... Well goodbye then, {}. I hope your life is full of misery <3. Happy Halloween!!!""" .format(your_name)) 

#also from (https://asciiart.website/index.php?art=holiday/halloween)
print("  .-.")
print(' (o o) boo!')
print(' | O \\')
print('  \   \\')
print("   `~~~'")
