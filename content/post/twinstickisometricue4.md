---
title: I Wanna Hold Your Hand... and Build a Twin Stick Isometric Game in Unreal Engine 4!
subtitle: there are a lot of tutorials out there for basic c++ games in unreal engine, but this one is mine
date: 2016-06-05
---

# Welcome to Games Camp

Hullo, I'm Calem, and welcome to the games camp!

In a few weeks (as of writing this) we'll be discussing programming as it related to video games both large and small for 4 days.
4 days isn't a lot of time, but it's enough time to learn some basic general programming and get an introduction to gaming development and logic.

This is a little introduction to the material that will be presented at the camp.
Most of the material that will be presented during the camp will only be given to you during the camp week; however, you should receive this little article, and a couple others, in an email before coming to the camp.
You don't need to read it ahead of the camp in order to do well in the camp, but I recommend you at least read this one and start thinking about the concepts presented.
Just a half hour or so of reading ahead can do a surprising amount of preparation.

There will be some varying skill levels from attendees of the camp.
While everyone will be asked to pay attention during the lecture periods, even if they know the material already, during the laboratory and project periods I will have a set of coding challenges prepared for people who finish the lab material early.

This page may be printed with reduced styling if you prefer reading from paper.
To print this page, just use the regular print menu in your browser.
Unfortunately that big

## Big Budget Games

<div class="uk-align-medium-right">
  <img style="width:600px;" src="/img/post/forhonor.jpg" />
</div>

Big budget games are massive endeavours.
They are typically done on a complicated gaming engine, such as Unreal Engine, Frostbite, or Anvil, and are developed by teams of hundreds of programmers, graphic designers, 3d artists, etc.
Looking at the below image, you might have a gameplay programmer make a scoring system, an animator else make the animation for someone swinging a sword, a physics programmer to write the physics for the sword hitting a target, a modeler to make the sword, an interface programmer to write the feedback to confirm a hit, etc.

Imagining for a moment we are programming the game, here's some of the stuff we might need:

1. A *list* of all the players
2. A set of *method*'s for getting the information from the player's controllers and moving their characters
3. A collection of *objects* representing everything in the game
4. Algorithms for lighting the scene
5. Drivers for displaying the game world to the player
6. A *loop* that continues the game until the player chooses to quit.

The list goes on!
But note those keywords, they're important.

**Usually** these sorts of games are blockbusters with interesting components and a fun core gameplay.
Lately they rely a lot on multiplayer, which has networking components.

## Tiny Budget Games

<div class="uk-align-medium-right">
  <img style="width:600px;" src="/img/post/limbo.jpg" />
</div>


These also go under the name of "indie games."
This type of game means a lot of different things to people.
Let's not get into that too much for now- perhaps during the lecture and discussion session we can talk about it.
What I want to bring to your attention is the difference between the below image of **Limbo** and the above image of **For Honor**.
**For Honor** uses a lot of textures, colors, and models to make a beautiful game.
**Limbo** uses some beautiful art assets, but they're 2D and black and white.


If you want to develop an indie game, you can get together with a friend and do it.
One of the beautiful things about video games is that you can "make a lot using a little."
When you're reading a book, maybe a vivid image of what's happening appears in your head.
When you're playing a game, just a little interaction can make a story that much better.
One popular phone game, **Tap Tap Revenge** involves players tapping their screens along with music- a simple game mechanic that was very enjoyable.

# Our Game

Over the next few days we're developing an AI for the game Space Racer.
Your AI will guide the ship through an asteroid field.

{{< img src="/img/post/spaceracer.png" title="McGill's Space Racer game." >}}

Our schedule consists of the following:

1. Learn basic programming
2. Explore 3D modeling
3. Learn about how different parts of game development fit together
4. Learn basic artificial intelligence for games
5. Hold a competition!

# Basic Programming

## What is programming?

A computer doesn't have any reasoning abilities or thought.
Not yet at least.
Any computer you use is following a list of instructions one by one.
If it does something other than that list of instructions, it has performed an error or its hardware has failed.
We call this list of instructions a *program*.
A program is an instruction set that tells the computer **exactly** what to do.
If a person wants to interact with the program, it needs to be prepared to receive *input*, such as whether a button on a controller is pressed.
For games, input is usually a pretty simple thing in which we check the current *state*, or its current set of conditions and data, on a gamepad.
Usually we interact with a computer through a screen such that the screen is the *output* of our program, but sometimes the output might be a paper printed out or a new file put on the computer's disk.

Even though a computer isn't sentient, not everything a computer does was necessarily written by a human.
Instead, it was probably written by a *compiler*.
A compiler is a program written to make programming easier.
This may be a little confusing at first, but most computers can only read 0's and 1's right now.
A program might look like 0010111010101011001011........
This isn't very easy to read or write.
Even the abstracted version of that code might look like this:

<pre>
  <code>
org
  xor ax, ax
  mov ds, ax
  mov si, msg
boot_loop:lodsb
  or al, al
  jz go_flag
  mov ah, 0x0E
  int 0x10
  jmp boot_loop
go_flag:
  jmp go_flag
msg db "hello world", 13, 10, 0
times 510-($-$$) db 0
db 0x55
db 0xAA
  </code>
</pre>

A program might consist of hundreds of thousands of lines of this sort of text, so programmers made an even *higher level abstraction* to represent the program.
After we made that higher level abstraction, we made another one!
For the most part, the higher level the abstraction, the less control you have over the final program, but the easier it is to make a useful program quickly.

If we compile the code above, it would produce a little program that prints "hello world" to the screen.
Another language can produce the same result with:

<pre>
  <code class="C++">
#include < stdio.h >
int main()
{
  printf("\nHello world!");
  return 0;
}  
</code>
</pre>

As programs grow larger and more complicated, the difference a higher level of language abstraction makes tends to also grow.
Having less control over the final program often means that the programs are slower though (during the camp, we'll talk about why this happens), so video games are often done in "low level languages."

## The Java Language

We're going to be learning the language Java.
Java typically isn't used for videogames, but it has wide industry use and the concepts in the language are the same as in the more popular languages for programming games, such as C++ and C#.
Right now, C# is best used on Windows.
C++ is simply impossible to learn in a week.
Fortunately, Java runs well on most platforms, uses similar principles as C# and C++, and is pretty easy to learn!

Java programs generally look something like this:

<pre>
  <code>
package gamescamp;

public class GamesCamp {

  public static void main(String[] args) {
      // TODO your code goes here
  }  
}
  </code>
</pre>

For the purpose of our camp, we're not going to talk about some of the above code.
We're interested in the segment `TODO your code goes here`.
The rest of it is basically telling the computer how to set up the program and where to start the program.

### A Walkthrough for Your First Basic Program

<pre>
  <code>
// this is a commented line
// it gives the reader notes
// you can comment your own code to make it easier to understand!
// or maybe to remind yourself of your own code later

package gamescamp; // ignore this

public class GamesCamp { // we can tell the computer this is
                         // the place to look for a main method

  public static void main(String[] args) { // the main method!
                                           // to the computer this looks like
                                           // "start here please"

    int countdown = 10;  // make a new integer variable and start it at 10
    for (int i = countdown; i > 0; i--)
      System.out.println("Launch in " + i);
  }  
}
  </code>
</pre>

Important key terms in the above segment:

- A *method* is a bit of functionality the computer can perform.  It might have some *input* and it might have some *output*.  Think about the mathematical `sine` function.  You usually say something like "the `sine` of pi is 0.0015."  In programming this is rephrased as "the method `sine` returns 0.0015 given the input pi."  
- A *variable* is like a placeholder for something you want the program to remember, like a sentence or a number.  Every variable has a *type* that tells the computer how to read the variable.

### Running a Java Program On Your Machine

When you come to the camp, the computers will already be set up to run your programs and the game we'll be using for AI easily.
