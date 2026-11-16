# HW1 notes

Answer each question in a few sentences. Be specific: name the function, the error or the command.

## What did you try?
I implemented the MenuItem class first, including its constructor, price property, and special methods. Then I worked on PromoItem using inheritance and super(). Finally, I implemented Order and cheapest() to calculate order totals and handle different objects.

## What broke, and how did you fix it?
I initially had to understand how property setters work and why I should use self.price instead of self._price in the constructor. I also had to be careful about aliasing when initializing the order's lines. I fixed this by creating a copy using list().

## What would you do differently next time?
I would plan the implementation before coding and test each method individually. I would also review Python concepts such as inheritance, composition, and duck typing before starting the assignment.