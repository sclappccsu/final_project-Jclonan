import random
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
quotes = [
    "With great power, comes great responsibility - Spiderman",
    "It's not who I am underneath, but what I do that defines me - Batman",
    "Intelligence is a privelege, and it needs to be used for the greater good of people - Dr. Octupus",
    "Heroes are made by the path they choose, not the powers they are graced with - Iron Man",
    "This. This is what I am. This is who I am come hell or high water. If I deny it, I deny everything I've ever done. Everything I've ever fought for - Green Arrow",
    "A hero can be anyone even a man doing something as simple and reassuring as putting a coat around a little boy's shoulder to let him know that the world hadn't ended - Batman",
    "You're going to make a difference. A lot of times it won't be huge, it won't be visible even. But it will matter just the same - James Gordon",
    "No man can win every battle, but no man should fall without a struggle - Spider-Man",
    "The future is worth it. All the pain. All the tears. The future is worth the fight - Martian Manhunter",
    "The universe is so big, it has no center. We are the center - Ms. Marvel",
    "Listen, smile, agree, and then do whatever you were gonna do anyway - Iron Man",
    "I think a hero is an ordinary individual who finds strength to persevere and endure in spite of overwhelming obstacles - Superman",
    "It's not dying that you need to be afraid of, it's never having lived in the first place - The Green Hornet",
    "You are much stronger than you think you are. Trust me - Superman",
    "Why do we fall? So we can learn to pick ourselves back up - Batman",
    "Everything doesn't have to be about fear. There's room in our line of work for hope, too -Batgirl",
    "What happens when the unstoppable force meets the immovable object? They surrender - Superman",
    "I need a day when there aren't twenty crises to deal with, but I don't see that coming any time soon - Iron Man",
    "The greatest power on Earth is the magnificent power all of us possess... the power of the human brain - Professor X",
    "I believe there's a hero in all of us, that keeps us honest, gives us strength, makes us noble, and finally allows us to die with pride - Spider-Man",
    "I'm here to fight for truth, and justice, and the American way - Superman",
    "A true hero isn't measured by the size of his strength, but by the size of his heart - Zeus",
    "Life doesn't give us purpose. We give life purpose - The Flash",
    "When you decide not to be afraid, you can find friends in super unexpected places - Ms. Marvel",
    "You only have your thoughts and dreams ahead of you. You are someone. You mean something - Batman",
    "Sometimes the truth isn't good enough. Sometimes people have got to have their faith rewarded - Batman",
    "No matter how many times you save the world, it always manages to get back into jeopardy again - Mr. Incredible",
    "The strength of this country isn't in buildings of brick and steel. It's in the hearts of those who have sworn to fight for its freedom - Captain America",
    "I know what it's like to not live up to expectations. To feel like nothing you do will ever be good enough - Green Lantern",
    "I have no idea where I'm going to be tomorrow but I accept the fact that tomorrow will come and I'm going to rise to meet it - Donna Troy",
    "I'm loyal to nothing, General... except the Dream - Captain America",
    "It's about what you believe. I believe in love. Only love will truly save the world - Wonder Woman",
    "The fate of your planet rests not in the hands of gods. It rests in the hands of mortals - Thor",
    "Sometimes you have to take a leap of faith first. The trust part comes later - Superman",
    "Violence doesn't discriminate. It comes as cold and bracing as a winter breeze and it leaves you with a chill you can't shake off - Daredevil",
    "Just because someone stumbles and loses their path, doesn't mean they can't be saved - Professor X",
    "Faith is my sword. Truth is my shield. Knowledge my armor - Dr. Strange",
    ]
message = random.choice(quotes)
twitter.update_status(status=message)
print("Tweeted: {}".format(message))