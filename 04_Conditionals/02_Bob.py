from helper import display_task_name, display_example

'''
Excersise: Bob
URL: https://exercism.org/tracks/python/exercises/bob

Instructions

Bob is a lackadaisical teenager. In conversation, his responses are very limited.

Bob answers 'Sure.' if you ask him a question, such as "How are you?".

He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).

He answers 'Calm down, I know what I'm doing!' if you yell a question at him.

He says 'Fine. Be that way!' if you address him without actually saying anything.

He answers 'Whatever.' to anything else.

Bob's conversational partner is a purist when it comes to written communication and always follows normal rules regarding sentence punctuation in English.
'''


def response(hey_bob: str) -> str:
    if hey_bob.isupper() and hey_bob.rstrip().endswith("?"):
        return "Calm down, I know what I'm doing!"
        
    elif hey_bob.rstrip().endswith('?'):
        return "Sure."
    
    elif hey_bob.isupper():
        return 'Whoa, chill out!'

    elif hey_bob.strip() == "":
        return 'Fine. Be that way!'
    
    else:
        return "Whatever."





# Test 1
display_task_name("I", "Bob > stating something")
display_example(
    'response("Tom-ay-to, tom-aaaah-to.")',
    'Whatever.'
)
print(response("Tom-ay-to, tom-aaaah-to."), "\n")




# Test 2
display_task_name("II", "Bob > shouting")
display_example(
    'response("WATCH OUT!")',
    'Whoa, chill out!'
)
print(response("WATCH OUT!"), "\n")




# Test 3
display_task_name("III", "Bob > shouting gibberish")
display_example(
    'response("FCECDFCAAB")',
    'Whoa, chill out!'
)
print(response("FCECDFCAAB"), "\n")




# Test 4
display_task_name("IV", "Bob > asking a question")
display_example(
    'response("Does this cryogenic chamber make me look fat?")',
    'Sure.'
)
print(response("Does this cryogenic chamber make me look fat?"), "\n")




# Test 5
display_task_name("V", "Bob > asking a numeric question")
display_example(
    'response("You are, what, like 15?")',
    'Sure.'
)
print(response("You are, what, like 15?"), "\n")




# Test 6
display_task_name("VI", "Bob > asking gibberish")
display_example(
    'response("fffbbcbeab?")',
    'Sure.'
)
print(response("fffbbcbeab?"), "\n")




# Test 7
display_task_name("VII", "Bob > talking forcefully")
display_example(
    'response("Hi there!")',
    'Whatever.'
)
print(response("Hi there!"), "\n")




# Test 8
display_task_name("VIII", "Bob > using acronyms in regular speech")
display_example(
    'response("It\'s OK if you don\'t want to go work for NASA.")',
    'Whatever.'
)
print(response("It's OK if you don't want to go work for NASA."), "\n")




# Test 9
display_task_name("IX", "Bob > forceful question")
display_example(
    'response("WHAT\'S GOING ON?")',
    "Calm down, I know what I'm doing!"
)
print(response("WHAT'S GOING ON?"), "\n")




# Test 10
display_task_name("X", "Bob > shouting numbers")
display_example(
    'response("1, 2, 3 GO!")',
    "Whoa, chill out!"
)
print(response("1, 2, 3 GO!"), "\n")




# Test 11
display_task_name("XI", "Bob > no letters")
display_example(
    'response("1, 2, 3")',
    "Whatever."
)
print(response("1, 2, 3"), "\n")




# Test 12
display_task_name("XII", "Bob > question with no letters")
display_example(
    'response("4?")',
    "Sure."
)
print(response("4?"), "\n")




# Test 13
display_task_name("XIII", "Bob > shouting with special characters")
display_example(
    'response("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!")',
    'Whoa, chill out!'
)
print(response("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"), "\n")




# Test 14
display_task_name("XIV", "Bob > shouting with no exclamation mark")
display_example(
    'response("I HATE THE DENTIST")',
    "Whoa, chill out!"
)
print(response("I HATE THE DENTIST"), "\n")




# Test 15
display_task_name("XV", "Bob > statement containing question mark")
display_example(
    'response("Ending with ? means a question.")',
    "Whatever."
)
print(response("Ending with ? means a question."), "\n")




# Test 16
display_task_name("XVI", "Bob > non letters with question")
display_example(
    'response(":) ?")',
    'Sure.'
    )
print(response(":) ?"), "\n")




# Test 17
display_task_name("XVII", "Bob > prattling on")
display_example(
    'response("Wait! Hang on. Are you going to be OK?")',
    "Sure."
)
print(response("Wait! Hang on. Are you going to be OK?"), "\n")




# Test 18
display_task_name("XVIII", "Bob > silence")
display_example(
    'response("")',
    "Fine. Be that way!"
)
print(response(""), "\n")




# Test 19
display_task_name("XIX", "Bob > prolonged silence")
display_example(
    'response("          ")',
    "Fine. Be that way!"
)
print(response("          "), "\n")




# Test 20
display_task_name("XX", "Bob > alternate silence")
display_example(
    'response("\t\t\t\t\t\t\t\t\t\t")',
    "Fine. Be that way!"
)
print(response("\t\t\t\t\t\t\t\t\t\t"), "\n")




# Test 21
display_task_name("XXI", "Bob > multiple line question")
display_example(
    'response("\nDoes this cryogenic chamber make me look fat?\nNo.")',
    'Whatever.'
)
print(response("\nDoes this cryogenic chamber make me look fat?\nNo."), "\n")




# Test 22
display_task_name("XXII", "Bob > starting with whitespace")
display_example(
    'response("         hmmmmmmm...")',
    "Whatever."
)
print(response("         hmmmmmmm..."), "\n")




# Test 23
display_task_name("XXIII", "Bob > ending with whitespace")
display_example(
    'response("Okay if like my  spacebar  quite a bit?   ")',
    "Sure."
)
print(response("Okay if like my  spacebar  quite a bit?   "), "\n")




# Test 24
display_task_name("XXIV", "Bob > other whitespace")
display_example(
    'response("\n\r \t")',
    "Fine. Be that way!"
)
print(response("\n\r \t"), "\n")




# Test 25
display_task_name("XXV", "Bob > non question ending with whitespace")
display_example(
    'response("This is a statement ending with whitespace      ")',
    "Whatever."
)
print(response("This is a statement ending with whitespace      "), "\n")