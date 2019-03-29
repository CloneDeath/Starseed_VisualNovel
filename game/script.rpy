define love = Character("Love")
define jacobs = Character("Jacobs", color="#75bb75")
define kid = Character("Random Kid", color="#999999")
define gray = Character("Grayson", color="#999999")
define max = Character("Max", color="#ffffff")
define patty = Character("Mrs. Patricia", color="#c3a38a")
define private = Character("Private Aaron", color="#757575")

define thug1 = Character("Red Haired Thug", color="#ff0000")
define thug2 = Character("Green Haired Thug", color="#00ff00")
define thug3 = Character("Blue Haired Thug", color="#4444ff")

define biker = Character("Biker", color="#bb8133")
define medic = Character("Medical Team Member", color="#ff9999")

define reporter = Character("Reporter", color="#816271")
define businessman = Character("Businessman", color="#505050")

transform left:
    yalign 0.30

transform right:
    yalign 0.30
    xalign 1.0

transform center:
    yalign 0.30
    xalign 0.5
    
transform gleft:
    yalign 0.0

transform gright:
    yalign 0.0
    xalign 1.0

transform gcenter:
    yalign 0.0
    xalign 0.5

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    "You wake up to the sound of someone yelling and banging what sounds like a frying pan."
    
    show private at center
    private "Everyone, up up up! Get up!"
    hide private
    
    show jacobs at right
    "Jacobs bursts into your bedroom."
    jacobs "Love, get up. We've finally got them!"
    hide jacobs
    
    "You get out of bed and head to the command center."
    
    scene bg command center
    show jacobs at right
    jacobs "A transport ship managed to trigger their silent alarm. The bandits don't even know we're coming."
    show love at left
    love "Awesome, let's go get them!"

    scene bg command center chase laser
    "After a fierce chase, you and your crew land a few hits on them, but they manage to get away."
    
    scene bg command center
    show love mad at left
    love "We lost them!"
    show jacobs at right
    jacobs "It's fine. It happens. Maybe it'll scare them off for good?"
    love "I doubt it."
    pause
    jacobs "Hey, let's call it a night and dock. We'll try again tomorrow."
    love "Alright..."
    
    scene bg ship landing
    "You and your crew land on the planet."
    
    scene bg town
    "After lunch, you and Jacobs wander around town, when you spot a small family shop."
    "You buy some local souvenirs, when you realize you forgot your coat back at the restaurant."
    show love at left
    love "I'll meet you back at the base. I won't be long."
    show jacobs at right
    jacobs "Alright, be back in time for dinner!"
    
    scene bg town night
    show love at left
    "You head your separate ways, retracing your steps."
    love "Wow, it sure is crowded at night."
    "You bump into someone."
    show love at center
    show thug1 at left
    thug1 "Ey, watch where ye'r goin'."
    love "Sorry."
    show thug2 at right
    thug2 "Yeah missss, you gotta keep your eyesss open."
    "A third thug butts in."
    show thug1 at left:
        xalign 0.0
    show love mad at center:
        xalign 0.3
    show thug2 at right:
        xalign 0.6
    show thug3 at right:
        xalign 1.0
    thug3 "Hey, you ain't from around here, are's ya?"
    "Scared, you back up. But the thugs keep getting closer, invading your personal space."
    love "Hey, umm... I'm sorry..."
    thug1 "Sorry ain't gunna' cut it."
    
    scene bg alley
    show thug1 at left:
        xalign 0.0
    show love mad at center:
        xalign 0.3
    show thug2 at right:
        xalign 0.6
    show thug3 at right:
        xalign 1.0
    "You look around, and realize you've backed yourself into an alley way."
    thug2 "Tisssk tisssk, ain't nowhere to run sssweety."
    hide love
    hide thug1
    hide thug2
    hide thug3
    
    show gray at gright
    kid "Hey, is there some sort of a problem here?"
    show thug2 at left
    show gray at gright
    thug2 "Keep walking, kid."
    hide gray
    "The green haired thug turns back to you."
    
    show thug2 at left with hpunch
    thug2 "Ow! What the..."
    show gray at gright
    "The kid had thrown a rock at the thug."
    
    show thug2 at center with move
    "The green haired thug pulls out a knife."
    show thug1 at left
    thug1 "Oi brat, ya hurt me friend sumfin' nasty."
    show thug2:
        xalign 0.8
    with move
    "The green haired thug manages to grab the kid."
    thug2 "You gotta learn sssome mannersss..."
    thug2 "And I got sssome learning you won't forget..."
    "The green haired thug hisses at the kid."
    show thug3 at center:
        xalign 0.3
    thug3 "Cut his ear off! That'll show the brat!"
    "The kid begins to cry."
    
    scene bg alley
    show max angry at right
    max "Let go of my {b}brother!{/b}"
    show thug2 at left
    with None
    show max angry at left:
        xalign 0.3
    with move
    "Max comes in swinging, knocking out the thug with the knife, and kicks it away."
    hide thug2 with dissolve
    max "Grayson, go get help! Hurry!"
    show gray at gright
    "The kid nods, wiping away his tears, and runs off."
    hide gray
    hide max
    
    show thug1 at center
    thug1 "You gotta lotta nerve guy..."
    hide thug1
    
    "You see your chance, and take it!"
    show thug3 at center
    show love mad at left:
        linear 0.2 xalign 0.3
    love "Hiya!"
    "You kick the blue haired thug in the shin, and sock him in the face, he falls down."
    show thug3:
        linear 0.3 rotate 45.0
    thug3 "Auauauaughhghh... What the hell happened?"
    hide thug3 with dissolve
    "Distracted, Max sucker punches the thug with red hair."
    show max angry at center:
        xalign 0.7
    max "C'mon!"
    "You run past the thugs. Max grabs your hand, and the two of you run into the crowd."
    
    scene bg town night
    "It isn't long before you find Grayson talking to some confused men in business suits."
    
    show max at center
    max "Grayson! There you are!"
    show gray at gleft
    gray "Brother! I found help!"
    businessman "Like I said, I don't think we're equipped to help, you really should find a..."
    
    max "No problem, sir. Sorry to bother you, but we've got it covered now. Thank you so much for your time."
    "The businessmen, confused, shrug and walk off."
    "Max looks to you."
    max "You should head home, you've had a rough time. Where do you live?"
    show love at right
    love "Not far... But, it's fine, I can-"
    gray "Hey, don't I get some sort of a reward???"
    max "Grayson!"
    "You laugh."
    max "In fact.. you do!"
    gray "Really?!"
    max "Yeah, you get to walk the young lady home."
    gray "awww..."
    "You and Max laugh."
    
    scene bg command center
    "Once you get back to the base, you tell Jacobs about the event."
    show love at left
    love "What was his name again?... Max!"
    show jacobs at right
    jacobs "Wow. Who knew the criminals here were so brave to try and mug an officer!"
    love "Ha ha, yeah..."
    "You spend the next few uneventful days in space, no bandit attacks."
    
    love "Maybe they got away? Jumped to a new system?"
    jacobs "It's possible, but not likely..."
    
    love "Why not?"
    jacobs "They'd either have to go through customs, or... well..."
    jacobs "For an unassisted trans-planetary departure, they'd need some serious hardware."
    love "Hmm... What stops them from just mimicking another ship?"
    jacobs "Nothing really, but the planetary egress logs would have duplicate departures and no re-entries..."
    love "I see..."
    "You have absolutely no idea what he's saying."
    jacobs "Wait... but... What if we did an in-flight scan... and..."
    "Jacobs begins to mumble to himself as he taps the computer screen."
    jacobs "We found him!"
    love "What? Where?"
    
    scene bg command center chase
    "You and your crew approach, but the ship fires blindly towards you and runs. Another pursuit ensues."
    
    scene bg command center chase cargo
    "While flying, a cargo ship gets stuck in the crossfire..."
    
    scene bg command center chase explosion
    "...and is destroyed."
    
    scene bg command center
    "This gives the bandits a chance to escape, as you search for survivors."
    "There are none."
    
    show jacobs at center
    jacobs "We'll keep looking for duplicate signatures, you need some time off."
    
    scene bg ship landing
    "You return back to the planet to take a day of vacation."
    
    scene bg town
    show love at center
    love "I was hoping we'd cross paths again, but..."
    "You spot a child with his nose pressed against a toystore window"
    love "Grayson? Grayson is that you!"
    "You run over, but... no. It's just some random kid."
    love "Sorry."
    "Your brief day-long vacation is over, and you head back to the ship."
    
    scene bg command center
    "As soon as you arrive, Jacobs flags you down."
    show jacobs at right
    jacobs "We've got him. They're cycling their signatures now, using docked ships to avoid duplication."
    show love at left
    love "How do we know?"
    jacobs "Log Deltas. I've gone ahead and set up a program to..."
    "You don't understand any of the techno-mumbo-jumbo he's saying."
    love "... right. Yes. Good. Checks out."
    "Jacobs stares at you for a moment."
    jacobs "So... Do we have permission to head out now?"
    love "Ohh! Yes! Right away!"
    
    "You all gather in the command center"
    love "This is our last chance. Innocents were killed last time."
    love "We can't let this keep going on."
    jacobs "The ship looks a little different... Some sort of upgrade, or modification?"
    jacobs "We should be more cautious, we don't know what they have outfitted."
    
    love "Can we get a closer look?"
    jacobs "Sure"
    pause
    scene bg command center chase
    show jacobs at right
    show love at left
    jacobs "aaaand we've been spotted."
    
    "The ship attempts to flee and you pursue."
    love "Private Aaron!"
    show private at center
    private "Yes mam?"
    love "Keep an extra eye out for civilians. Make sure none come between us. I..."
    love "I don't want a repeat of last time."
    private "Yes mam!"
    hide private
    
    "The pursuit continues, until they are cornered."
    love "Aim for their engines."
    
    scene bg command center chase laser
    show jacobs at right
    show love at left
    "The enemy ship jerks, and your team misses their engines. Unfortunately, for them, it hits their hull, doing massive damage."
    love "Hail them again, demand surrender."
    love "Private Aaron!"
    show private at center
    private "Me?"
    private "Ahem... I mean..."
    private "Yes mam?"
    love "Get medics on standby."
    private "But... "
    private "No one is hurt. Everyone is fine..."
    jacobs "Not for us you idiot! Them! We want them in custody, not dead!"
    private "R-... right!"
    "Private Aaron runs off."
    
    scene bg command center chase
    show jacobs at right
    show love at left
    jacobs "Captain! Look!"
    "The bandit craft shuts down, and motion can be seen inside through some windows."
    
    love "Do you think their comms are down?"
    jacobs "Possibly..."
    love "Keep an eye out for a signal. A white flag..."
    
    "In an instant, there's a flash, and two pods jettisons from the craft, rapidly approaching the planet:"
    "One small escape pod, and a large cargo pod."
    
    love "Wha-- -what?!"
    love "After him!"
    jacobs "But, what about the ship? There could be other casualties..."
    love "I didn't... you're... you're right. Get the med team suited up. They're going in."
    
    "No one is found aboard the craft. The sole pilot jettisoned, and got away. Once again."
    
    jacobs "This will at least stop him from plundering trade ships."
    love "Yes. But this is the third time we've let the same bandit get away..."
    
    scene bg ship landing
    "After a few more uneventful days, Love docks back onto the surface for her scheduled leave."
    
    scene bg town
    show love at left
    love "I can't believe I let him get away..."
    show max cast at right
    max "Let who get away?"
    love "Max! I- I didn't think I'd see you again!"
    max "Heh, why? What's up?"
    love "I never got to thank you... you and your brother..."
    show gray at gcenter
    gray "You can thank me with icecream!"
    "Everyone laughs, and you all agree to get some icecream."
    
    scene bg town night
    show love at left
    show max cast at right
    "Grayson eventually heads home, leaving you and Max alone to share a warm evening in the park."
    
    love "I forgot to ask, what happened to your arm?"
    "Max's arm is in a cast."
    max "Ohh, this? Ha, well... it's a... work hazard I presume? ha ha"
    
    "Love suddenly has flashbacks to the shot down ship, and the ejected pods."
    love "What... what exactly do you do?"
    max "This and that, I'm a bit of a freelancer, I suppose."
    love "Ohh... and... your arm..."
    love "Was there... a fight?"
    max "Eh, you could say so"
    pause
    max "But I have to admit, it was pretty one sided. You can imagine who lost."
    pause
    
    love "Max....."
    max "Yeah?"
    love "What... What exact--"
    "Love is cut off by someone yelling in the distance."
    show gray at gcenter
    gray "Max! Max! He's back! And he's causing a scene!"
    max "Not this guy again. Umm... this won't take long."
    "Max gets up"
    max "You, uhh, you're welcome to come with. It won't take long, I promise."
    "You agree"
    
    "Max grabs your hand and leads you out of the park, back into town."
    
    scene bg town night
    show max cast at right
    max "Sorry, we gotta get there quick."
    "You nearly trip over the un-even sidewalk. You're definitely in the rundown part of town."
    
    max "Hey, asshole!"
    show biker at left
    biker "Wha? Who you calling asshole?"
    max "You, asshole! I told you, you're not welcome here anymore! We've given you enough chances, now scram!"
    biker "Look. Max. Listen..."
    max "No, you look here. We've given you more than enough chances, and you've blown them all."
    biker "But, Max..."
    max "Don't 'But Max' me. It ain't happening. Get. Out."
    "The biker looks down, defeated."
    "He slowly gets back onto his bike."
    max "Hey."
    biker "Hmm?"
    max "Next week. One more chance. ONE."
    "The biker smiles, starts up his bike, and heads off."
    hide biker
    
    show love at left
    love "Um... what was that about?"
    max "Him? He's just got a few too many knocks to his head. Can't quite tell right from wrong anymore."
    
    "You follow Max into the shop, and..."
    
    scene bg kitchen
    "You're overwhelmed with the most delicious smells! Spices! Herbs! Cheeses!"
    show gray at gcenter
    gray "Today's 'Italy day'!"
    show max cast at right
    max "It's called 'Italian Day' Grayson. Today we're serving Italian food, specifically, spaghetti and garlic bread."
    show love at left
    love "It's... a homeless shelter?"
    max "Yeah, and a Kitchen. I've been volunteering here lately. It's not much, but it's good work!"
    gray "The place was about to shut down before Max and I stepped in!"
    max "Ha, no way!"
    max "Mrs. Patricia would have found a way to keep the place running."
    
    love "Ohh! So your arm...? I'm still a little confused..."
    max "I mean, you saw the guy out there? Let's just say not everyone is noble and kind-hearted as Grayson here."
    "Max pats Grayson on the head."
    gray "Yeah! I'm going to grow up to be a policeman!"
    max "Ha... I'm... still working on convincing him out of that one."
    "Everyone laughs."
    
    scene bg kitchen with dissolve
    "Love spends the next few days with Max, volunteering at the shelter, and growing ever closer."
    
    scene bg town night
    "They spend the final evening of her leave in the park, watching the sun set."
    
    show love at left:
        xalign 0.3
    love "I can't believe this is my last day."
    show max at right:
        xalign 0.7
    max "So what? You'll be back after another week. And I'll be here, waiting for you."
    love "Waiting for me?"
    max "I mean--"
    "He blushes."
    max "I mean me and Grayson, and Mrs. Patricia... you've helped out so much these past couple days."
    "You blush."
    
    love "Well..."
    love "I better be off."
    max "Yeah. I'll... I'll miss you."
    pause
    show gray at gright
    gray "Are you two going to kiss now?"
    max "Grayson! What are you doing here!"
    gray "Mrs. Patricia said I should keep an eye on you two, and make sure you don't get into trouble."
    max "Get out of here! I'll be home soon."
    hide gray with dissolve
    "Grayson runs off"
    love "I guess..."
    max "I guess this is goodbye, I'll..."
    love "I'll see you in a week."
    "You two hold hands. And..."
    hide max with dissolve
    "He lets go..."
    hide love with dissolve
    "And you walk away..."
    pause
    
    scene bg bedroom
    "You think about him that night, for the rest of the night."
    show love at right
    love "When I get back... I'll tell him. I'll tell him how I feel."
    hide love with dissolve
    
    "A couple days pass. Nothing interesting happens."
    
    scene bg command center
    show jacobs at right
    jacobs "Um... hmmm... this is odd"
    show love at left
    love "What is it?"
    jacobs "That ship, over there... it doesn't match its signature. It's off..."
    love "So? Maybe the signal-"
    jacobs "There's more... it looks like this ship was recently stolen from a junkyard."
    love "So... Just to be clear: Someone stole a hunk-of-junk, and doesn't want anyone to know?"
    jacobs "Yup"
    love "Let's flag him down!"
    
    scene bg command center chase junk
    "As your crew approaches, the ship notices, and takes off."
    show love at left
    love "Are you serious?"
    show jacobs at right
    jacobs "It's clearly a stolen vehicle, the punishment for that is pretty stiff. What did you expect?"
    scene bg command center chase junk busy
    show love at left
    show jacobs at right
    love "The place is extremely crowded."
    love "Last time... someone got in the way..."
    jacobs "I know."
    love "Innocents died."
    jacobs "I know."
    love "..."
    love "...let him go."
    scene bg command center busy
    show love at left
    show jacobs at right
    pause
    jacobs "I agree, captain."
    hide jacobs
    show private at right 
    with dissolve
    private "... Me too captain. I don't think it's worth the risk."
    hide private
    with dissolve
    love "Thanks. I... I believe we did the right thing."
    
    scene bg command center
    with dissolve
    "You spend the rest of the day thinking about the incident. Was it the right thing?"
    
    show jacobs at right
    jacobs "We've got a problem."
    show love at left
    love "What's up?"
    jacobs "We've got an emergency report, a transport ship has been robbed."
    jacobs "Seems there was a struggle. One casualty, the pilot."
    love "These asshole bandits.. They just don't care..."
    love "You heard him crew, let's go!"
    show private at center
    private "Yes m'am!"
    hide private
    jacobs "There's... there's more Love."
    love "What is it?"
    jacobs "According to the co-pilot, the bandit's vehicle matches the description of the... um... \"hunk of junk\" we let go earlier."
    show love mad at left 
    pause
    jacobs "Are you... Are you okay Love?"
    love "Yes. Let's... Let's just do our job, okay?"
    
    "You and your crew head to the scene, and patrol the area for a few hours."
    jacobs "I got him. Right here."
    love "Where?"
    jacobs "Here, on the edge of our scanners, a signal change. I saw it with my own eyes. The logs confirm."
    jacobs "This vehicle is illegally changing signals."
    love "Let's go."
    
    scene bg command center chase junk
    "You approach the signal, and the ship quickly comes into view."
    
    show love mad at left
    love "That's it. That's him."
    show jacobs at right
    jacobs "What do we do? We haven't been noticed."
    love "Send a message. Tell him to surrender."
    jacobs "... Yes mam."
    jacobs "..."
    jacobs "Sent."
    "Everyone waits in silence."
    jacobs "The ship, it's engines are starting up. I believe it's trying to flee."
    love "Open fire."
    jacobs "Roger."
    
    scene bg command center junk damage
    with hpunch
    
    "Your crew gives off a warning shot, but causes severe damage to the ship."
    
    show love mad at left
    love "What happened!?!"
    show jacobs at right
    jacobs "Umm... It.. It looks like the ship has no shields."
    love "What the hell??? It's illegal to fly a ship without even basic shielding! What if a piece of space junk hit him?"
    jacobs "Love, the ship was stolen from a junkyard... maybe the thief didn't know..."
    love "Get a medical team out there right away! We need to make sure he's alive, and in custody. NOW!"
    
    scene bg command center junk damage
    with dissolve
    "Everyone scatters, as Love listens closely to their transmissions."
    
    medic "This looks bad."
    pause
    medic "The external hatch is stuck. Electronics are down. Life support is down."
    medic "I'm torching the door."
    pause
    medic "No de-pressurization."
    pause
    medic "One body."
    medic "No suit."
    pause
    medic "That's it. One casualty, and no survivors."
    
    "Love is visibly pissed."
    show jacobs at right
    jacobs "To be fair... the transport... he... I mean, he did..."
    show love mad at left
    love "That's no excuse. We made {i}SO{/i} many mistakes today. I can't even begin to think about all this."
    
    scene bg command center
    "The rest of the week passes without incident."
    "There was a judicial review of the events that unfolded."
    "The crew is not found accountable for either death."
    "\"There's no way anyone could have known\""
    "Despite this, a controversy persists in the media for days."
    "You and your crew refuse to talk to the press."
    
    scene bg ship landing
    "You and Jacobs take your leave a day early, heading back to the planet."
    
    scene bg town
    "You head directly to the shelter."
    "All you can think about is what you've done... and Max."
    "Would he forgive you? Could he?"
    "You slow down... take your time."
    "You're just delaying the inevitable."
    
    scene bg kitchen
    "But, eventually, you get there. The shelter."
    show gray at gright
    gray "Love! You're back early!"
    show love at left
    love "Yes, I am."
    "She forces a smile."
    love "Where's max?"
    gray "He still isn't back. He went on some errand for Mrs. Patricia."
    love "Right..."
    
    "A few hours pass, when Love finally spots Mrs. Patricia."
    
    love "Patty! Hey!"
    patty "Hello Love! You're back early!"
    love "Yes, I couldn't wait. Where's Max? I haven't seem him all day."
    "The smile leaves Mrs. Patricia's face"
    patty "Um, come with me Love."
    "You follow her into the next room, as Grayson gets up."
    patty "No, you stay right there Mr."
    patty "Us adults need a moment to talk."
    gray "Aw man..."
    "He sits back down."
    
    love "What... what is it Mrs. Patricia?"
    patty "... did, Max ever tell you what he did for a living?"
    love "Yes... he volunteers here. He feeds the homeless. He helped save the place."
    "Mrs. Patricia's eyes begin to well up as she smiles."
    patty "Yes. Yes he did..."
    patty "Did he ever tell you {i}how{/i} he saved the place?"
    love "No."
    patty "Love. I... I don't know what to say."
    love "What... Why? What happened?"
    patty "Max. He's a good kid. His heart was always in the right place."
    patty "We had no money. We had no way to buy food. We could barely afford rent as it is."
    patty "I could have just gotten another job, but..."
    patty "All those hungry people that come by here everyday... the starving poor..."
    patty "Some of them are children..."
    patty "Then, one day, Max kicks in the door..."
    "Mrs. Patricia smiles"
    patty "I'll never forget, he said something like..."
    patty "\"M'am, I heard you're in need of a hero\""
    patty "You have to understand,"
    patty "I had no idea who he was at the time, and he just barges in like that.."
    "She laughs."
    patty "I attacked him with a frying pan. I thought he was just some hooligan, looking to start a fight."
    "She's quiet for a moment."
    patty "He had a whole truckload of food for us. Various grains and cereals, vegetables, meats..."
    patty "It was the most generous donation we've ever received."
    "Both of you smile."
    patty "But good things don't last forever. We had enough money to afford the place, but ran low on food again."
    patty "A couple days pass, and \"Miracle Max\" pops by again with a full truck and a broken arm!"
    patty "He needed a cast, but all he cared about was getting the truck unloaded before the food spoiled!"
    "Mrs. Patricia sighs."
    patty "He told me... He told me what happened."
    patty "Who he really was."
    "You see a shadow move beneath the door."
    patty "Grayson...!"
    "The door slowly opens."
    gray "Yes, mam?"
    patty "Were you evesdropping again?"
    gray "Yes mam..."
    "He looks down."
    "Mrs. Patricia lets out a long sigh."
    patty "Come here boy,"
    patty "We're talking about your brother."
    "Grayson's face lights up."
    gray "We are!?"
    "He excitedly runs over."
    gray "Did he ever tell you about the time he fought off over a hundred pirates! All on his own!"
    patty "Not now, Grayson."
    patty "Come, sit down next to Love."
    "Grayson excitedly pulls up a chair and sits."
    patty "So, as I was fixing his broken arm..."
    gray "Ohh! I know this one! Robinhood!"
    patty "Yeah... that's what he said. What he called himself. He told me that the food was stolen."
    patty "He'd steal the food from transport ships, and brought it here."
    "There is a silence in the room."
    gray "But it was for the greater good! To help people! Brother wouldn't hurt nobody!"
    patty "That's right. Your brother wouldn't harm a fly. Because of him... we were able to help so many people..."
    patty "I... so..."
    patty "So, we're low on food again. He insisted on getting more."
    patty "I told him no, it's dangerous, there's got to be a better way,"
    patty "But he insisted."
    patty "He said, \"One more\"..."
    patty "\"One more, then we'll find a better way\""
    "She begins to tear up again."
    patty "He... stole a ship from some junkyard."
    patty "He specifically picked out the \"biggest piece of junk\" there was. Something no one would miss."
    patty "\"Just think of it as borrowing.\" he said \"I {i}will{/i} give it back, I {i}promise{/i}. No one will even know it went missing.\""
    patty "I... I don't know exactly what happened after that."
    patty "But, based on the news... I guess there was a struggle."
    patty "Someone got killed."
    patty "Because of that... They... the officers... they killed him."
    patty "Blew his ship up with him still in it."
    patty "They didn't even..."
    "She stops herself."
    "The room is silent."
    patty "I'm... I'm sorry Grayson. I'm sorry I couldn't tell you before."
    "Mrs. Patricia begins crying"
    patty "Your brother. Max. Max is dead."
    pause
    "You race back to the base, as fast as your legs can carry you."
    "Mrs. Patricia calls after you, but you keep running."
    love "No. No... I couldn't have... I didn't... I didn't know."
    "Out of the corner of your eye, you see his face."
    love "Max!"
    "The television screen flickers as the reporter continues..."
    reporter "... killing young Max."
    reporter "We tried reaching out to Captain Love Sonos and her crew, but they refused to comment on the event."
    pause
    "Love weeps."
    "{b}The end.{/b}"
    pause
    return