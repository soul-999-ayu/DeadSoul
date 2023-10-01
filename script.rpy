# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ayush")
define e = Character("Priya")
define n = Character("Nikhil")

# The game starts here.
label start:
    "**You are playing as Ayush**"
    ""
    play music "illurock.opus"
    image pic = im.Scale("one.png", 1920, 1580)
    show pic
    "You woke up at 5:45AM"
    "You are still feeling sleepy."
    show bedroom
    "You sat on your sofa and start thinking about a girl."
    a "P............"
    a "Pri............"
    a "Priy............"
    a "Priya............"
    "You dove deep into her thouhts."
    "You closed your eyes and got a thought to go to the park"
    scene school
    "You went to park to roam around."
    "************** IN PARK **************"
    show priya
    e "Heyy Ayush!."
    e "How are you?"

    menu:
        "Welllll... I, I, I'm Good.":
            show priya blush
            e "Glad to hear that"
        "I'm depressed.":
            show priya tear
            e "Ohhhhhh, I'm feeling sorry"

    show priya norm
    a "How are you btw?"
    show priya good
    e "I'm Good."
    "..."
    "Ayush(In thoughts): Should I ask her to be my friend?"
    "..."
    show priya angry
    "What if she says NO!"
    show priya blush
    "What if she says Yes!"
    "..."
    "Ayush(In thoughts): Sould I ask her?"
    show priya norm
    menu:
        "Yes, I should.":
            "Ayush (In thoughts): Lemme gather some confidence"
            a "Ahh, I wanna ask you something."
            e "Yes"
            a "Will you be my friend?"
            show priya blush s
            e "ummmmm..."
            show priya blush
            e "Why not!?!"
        "No, She'll refuse.":
            "..."
            e "I wanna ask you something."
            a "Yes."
            show priya blush
            e "Will you be my friend?"
            a "Wwhhhh, Why not?"
            e "Thats nice of you."
    ""
    "Suddenly you saw a random person approaching towards you."
    show priya norm at left
    show normal at right:
        zoom 0.3
    ""
    show normal at right:
        zoom 0.45
    "Yoy recognized him right away, he's the best friend of Priya."
    "He's a good guy, just like her."
    show ask at right:
        zoom 0.45
    n "You're our senior, right?"
    a "Yes, I am."
    show conf at right:
        zoom 0.45
    a "Are you her best friend?"
    show think at right:
        zoom 0.45
    n "Ummm.."
    ""
    scene school
    show priya norm at left
    show normal at right:
        zoom 0.45
    n "Yes, I am, but she does not consider me as her best friend."
    show priya at left
    e "Why should I?"
    show mad at right:
        zoom 0.45
    n "What do you mean?"
    a "oohhkkk oohkkk"
    a "Stop you two, this is not a place to fight."
    scene school
    show priya norm at left
    show normal at right:
        zoom 0.45
    n "Hey Priya, can you let us talk for two minutes?"
    e "What do you want to talk about?"
    show ohman at right:
        zoom 0.45
    n "Nothing, just leave us  for 2 minutes."
    e "Okay."
    scene school
    show normal:
        zoom 0.45
        xalign 0.5
    n "Bro, I'm giving you a dare."
    a "Giving me what?!?"
    show confident:
        zoom 0.45
        xalign 0.5
    n "You have to say 'I Love You' to priya."
    a "What?"
    show shut:
        zoom 0.45
        xalign 0.5
    n "Please do it, I want to see her reaction."
    a "Umm, ohk, lemme gather some confidence."
    show normal:
        zoom 0.45
        xalign 0.5
    n "Priyaaaaaaaaaaaaa, come here."
    scene school
    show priya norm at left
    show normal at right:
        zoom 0.45
    a "Hey Priya."
    e "Yes."
    a "I wanna say something."
    show conf3 at right:
        zoom 0.45
    show priya good at left
    e "What is it?"
    a "I.."
    a "I.."
    a "I Love You!"
    show priya blush s
    e "Whhhhaaaaaaaaaatttttttttttt?"
    e "Are you sure?"
    a "Yes, I am."
    show priya blush
    e "I love you too."
    show mad at right:
        zoom 0.45
    a "Reallllllllllyyyyyyyyyyyy???????????"
    "**Her voice got trapped inside your head**"
    "**I love you too**"
    "**I love you too**"
    "**You started falling backward**"
    image pic3 = im.Scale("bg/sky.png", 1920, 1580)
    scene pic3
    show school:
        ypos 650
    show priya serious
    e "Are you fine?"
    a "I, I, I'm not."
    scene pic3
    a "Hellllpppppp..."
    image pic4 = im.Scale("bg/dissolve bg.png", 1920, 1580)
    scene pic4
    "**You passed out**"
    show bedroom with fade
    "**You wakes up on your sofa and realizes that it was all a dream**"
    a "Wooo! The dream was awesome, I wish it will come true someday."
    ""
    # This ends the game.

    return
