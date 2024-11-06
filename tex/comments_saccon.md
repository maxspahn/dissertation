## Intro

This is a timely work related to reactive motion generation for mobile
manipulators in partially-structured dynamic environments. I have enjoyed
reading the whole manuscript and appreciated the healthy combination of
theoretical, numerical, and experimental aspects, with an eye towards practical
implementability and with clear highlighting of advantages and remaining
limitations.


## MINOR COMMENTS 

I would suggest to refer to the environments of interest as semi-structured
dynamic environments. By itself, a dynamic environment could be totally
predicable, thus presenting limited challenges for planning. The challenges
emerge in presence of uncertainty (structured vs. unstructured).
-> semi-structured and human-shared as a special case? DONE

It would be potentially benefit to slightly revise Chapter 2, to make sure it is
self-contained. In particular, to define what a Finsler structure is explicitly,
instead of asking the reader to fetch the publications related to Optimization
fabric to understand the concept (and the related  "energization" operation). 
-> Explicit state properties of finsler DONE

In the Chapter 3, I would appreciate a closer look at approaches such as
Dynamical System approach developed, among other places, at EPFL and a more
in-depth (qualitative) comparison with the concept of optimization fabric. I
regard these approaches as quite similar (but being no expert) and therefore it
would be of value to get better insights in the main differences.
-> comparison to dynamic systems DONE in related works

One aspect that could also be improved is to explicitly discuss the need to
define a trajectory to follow for a robot. Somehow, this seems to comes from
control theory (in particular, trajectory tracking) but it is unclear if this is
a good paradigm also for robots in unstructured environments or robots that are
tasked to interact physically with the environment. 
-> I think he refers to trajectory but means path, in the sense that path
following. In the introduction we can add a sentence or two for local minima

One aspect I am missing in the introduction is a also discussion about
making/breaking of contact with the environment, and its potential connection
with the optimization fabric approach. Furthermore, it might be worth mentioning
that collision avoidance might not be the only option in unstructured
environments: what about collision/contact exploitation? I appreciate that this
point of view is actually reflected in the propositions of the author (and I am
unfortunately not so confident about the truth of proposition 9).
-> adding subsection on exploring contacts before 1.1 potentially
-> Add more in the conclusion

The thesis seems to emphasize human-robot co-existence. It could be work
mentioning that the work is also of potential interest for full autonomy in
unstructured environment, with no human (operators) sharing the workspace. 
-> Can the introduction be changed make human-shared a specific case of
unstructured?

There is a comment in Section 1.2 mentioning that computations are efficient
because of the geometry: I did not found it very apparent why that should be the
case and what is meant with efficient.
-> No optimization requered at the end of 1.2 DONE

In Chapter 5, the concept of dynamic fabric is introduced. I must confess that I
was expecting a closer connection with classical analytical mechanics. Although
I have a background in differential geometry, I got a bit lost in trying to
follow the mathematical aspects in Section 5.2.4, and understand what is the
core new result. I think this is particly caused by some inaccuracies in the
mathematical writing such as, e.g., the missing of the definition of the set
X_{rel} in Def. 5.2.2 that appears to be a time-varying set (?), given that ilde
x is a trajectory. I have also some issues in understanding the logic in the
definition of \phi_d: X x X -> X_rel and its connection with the new definition
of the dynamic pull back in (5.1). But this is something that we could address
during the defense, given that the chapter in question is apparently already
being accepted for publication as is.
-> part of a verbatim copy

As a general remark, I would suggest to be more explicit in defining the
dimension of the variables, such as, e.g., in (5.9), where I could also not
immediately grasp what is the "root velocity of the fabric" (the term "root
velocity" does not seem to appear anywhere else in the thesis).  Another example
of potential improvement in the mathematical writing is in Chapter 7, where by
phi_{sdf}(fk) the candidate likely mean phi_{sdf}(FK(\cdot)) or equivalently
phi_{sdf} \circ FK (with \circ denoting function composition).
-> part of a verbatim copy

Besides those minor aspects, the overall work appears to be solid and I found
particularly useful the approach of autotuning the dynamic fabric parameters by
Bayesian optimization. I am looking forward to the oral defence to have
additional time to discuss the topics addressed in the manuscript.

 

 
