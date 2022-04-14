print('''                                                     ___
                                                  .~))>>
                                                 .~)>>
                                               .~))))>>>
                                             .~))>>             ___
                                           .~))>>)))>>      .-~))>>
                                         .~)))))>>       .-~))>>)>
                                       .~)))>>))))>>  .-~)>>)>
                   )                 .~))>>))))>>  .-~)))))>>)>
                ( )@@*)             //)>))))))  .-~))))>>)>
              ).@(@@               //))>>))) .-~))>>)))))>>)>
            (( @.@).              //))))) .-~)>>)))))>>)>
          ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>
       ((  ((@@@.@@             |/))))) //)))))>>)))>>)>
      )) @@*. )@@ )   (\_(\-\b  |))>)) //)))>>)))))))>>)>
    (( @@@(.@(@ .    _/`-`  ~|b |>))) //)>>)))))))>>)>
     )* @@@ )@*     (@) (@)  /\b|))) //))))))>>))))>>
   (( @. )@( @ .   _/       /  \b)) //))>>)))))>>>_._
    )@@ (@@*)@@.  (6,   6) / ^  \b)//))))))>>)))>>   ~~-.
 ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \b/)>>))))>>      _.     `,
  ((@@ @@@*.(@@ .   \^^^/' (  ^   \b)))>>        .'         `,
   ((@@).*@@ )@ )    `-'   ((   ^  ~)_          /             `,
     (@@. (@@ ).           (((   ^    `\        |               `.
       (*.@*              / ((((        \        \      .         `.
                         /   (((((  \    \    _.-~\     Y,         ;
                        /   / (((((( \    \.-~   _.`" _.-~`,       ;
                       /   /   `(((((()    )    (((((~      `,     ;
                     _/  _/      `"""/   /'                  ;     ;
                 _.-~_.-~           /  /'                _.-~   _.'
               ((((~~              / /'              _.-~ __.--~
                                  ((((          __.-~ _.-~
                                              .'   .~~
                                              :    ,'
                                              ~~~~~
''')
print("Welcome to Dragon Treasure.")
print("In this adventure, you have to figure out how to get the treasure that is guarded by an enormous dragon.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You go through a dense forest and there two paths and you must choose between left and right.")
first_step = input("What path do you choose? (type right or left)\n")

if first_step.lower() == 'left':
  print('You pass the first test, you are save!!!\n')
  print('Now, you see a castle in the distance and when you approach it, you figure out that the castle is surrounded by water. There is a door that you can reach swimming or jumping with a pole.')
  second_step = input("What do you do swimming or jumping? (type swimming or jumping).\n")
  if second_step.lower() == 'jumping':
    print('You pass the second test, you are save!!!')

    print("You hear some roars and you go to them, so you discover that there is an enormous fluffy dragon guarding a huge amount of gold coins.")
    print("Next to you, there is a big comb, a sharp sword and a heavy mace.")
    third_step = input("What item do you choose? (type comb, sword or mace).\n")
    if third_step.lower() == 'comb':
      print("You win!!! The dragon wants someone to care of him. He allows to you to get some coins.")
    else:
      print("Game over!!! Dragon is immortal and cannot be killed. It gets so angry, it burns you.")
    
  else:
    print('Game over!!! You are being eaten by piranhas.')

else:
  print('Game over!!! You are stuck in a mud lake and it is impossible that you can get out of it.\n')

