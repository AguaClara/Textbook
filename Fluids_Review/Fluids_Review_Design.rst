.. _fluids_review_design:

************************
Fluids Review  Design
************************

Welcome to the **first** summary sheet of CEE 4540! These documents will
be guides and references for you throughout the semester. Since
Professor Monroe’s class time is limited, so too is the amount of
material he can fit on the slides while ensuring that they remain
understandable. Thus, these summary sheets will supplement the
powerpoints by going into further detail on the course concepts
introduced in the slides.

Equations, universal constants, and other helpful goodies can be found
in the `aide_design repository on
GitHub <https://github.com/AguaClara/aide_design/tree/master/aide_design>`__.
Most equations and constants you find in these summary sheets will
already have been coded into aide_design, and will be shown here in the
following format:

| Variable: ``pc.gravity``
| Function: ``pc.area_circle(DiamCircle)``.

The letters before the ``.``, in this case ``pc``, indicate the file
within aide_design where the variable or function can be found. In the
examples above, ``pc.gravity`` and ``pc.area_circle(DiamCircle)`` show
that the variable ``gravity`` and function ``area_circle(DiamCicle)``
are located inside the
`physchem.py <https://github.com/AguaClara/aide_design/blob/master/aide_design/physchem.py>`__
(``pc``) file. You are strongly recommended to look up any aide_design
equations you plan to use within in their aide_design file before using
them, even if they are given here in this summary sheet. This is because
each equation has comments in its original file describing what the
specific conditions are to using it.

For the most part, `hyperlinks in these documents will contain
supplementary information <http://likethis.com/>`__. The information
contained in the linked external sites is there in case you don’t feel
completely comfortable with a concept, but is not necessary to learn
thoroughly and will not be tested.

--------------

.. _section-fluids-review-1:

Section: Fluids Review
========================

This section is meant to be a refresher on fluid mechanics. It will only cover the topics of fluids mechanics that will be used heavily in the course.

If you wish to review fluid mechanics in (much) more detail, please refer to `this guide <https://github.com/AguaClara/CEE4540_Master/wiki/Fluids-Review-Guide>`_. If you wish to review from the textbook used in CEE 3310, the intro to fluid mechanics course at Cornell, you can find a pdf of the book `here <https://hellcareers.files.wordpress.com/2016/01/fluid-mechanics-seventh-edition-by-frank-m-white.pdf>`_.

Important Terms
-----------------

1. Head
2. Streamline
3. Head loss
4. Laminar
5. Turbulent
6. Moody Diagram
7. Viscosity
8. Driving head
9. Vena Contracta/Coefficient of Contraction

Important Equations
--------------------

1. Bernoulli equation
2. Energy equation
3. Darcy-Weisbach equation
4. Reynolds number
5. Swamee-Jain equation
6. Hagen-Poiseuille equation
7. Orifice equation

Introductory Concepts
=======================

Before diving in, there are a few important concepts which will be the
foundation for building your understanding of fluid mechanics. One must
walk before they can run, and similarly, the basics of fluid mechanics
must be understood before moving on to the more fun sections of this
document.

Continuity Equation
----------------------

Continuity is simply an application of mass balance to fluid mechanics.
It states that the cross sectional area :math:`A` that a fluid flows
through multiplied by the fluid’s average flow velocity :math:`\bar v`
must equal the fluid’s flow rate :math:`Q`:

    .. math::

      Q = \bar v A

.. note:: The line above the :math:`v` is called a ‘bar,’ and represents an average. Any variable can have a bar. In this case, we are adding the bar to velocity :math:`v`, turning it into average velocity :math:`\bar v`. This variable is pronounced ‘v bar.’

In CEE 4540, we deal primarily with flow through pipes. For a circular pipe, :math:`A = \pi r^2`. Substituting diameter in for radius, :math:`r = \frac{D}{2}`, we get :math:`A = \frac{\pi D^2}{4}`. You will often see this form of the continuity equation being used to relate the flow rate in a pipe to the fluid velocity and pipe diameter:

    .. math::

      Q = \bar v \frac{\pi D^2}{4}

The continuity equation is also useful when flow is going from one geometry to another. In this case, the flow in one geometry must be the same as the flow in the other, :math:`Q_1 = Q_2`, which yields the following equations:

    .. math::

      \bar v_1 A_1 = \bar v_2 A_2

    .. math::

      \bar v_1 \frac{\pi D_1^2}{4} = \bar v_2 \frac{\pi D_2^2}{4}

| Such that:
| :math:`Q =` fluid flow rate
| :math:`\bar v =` fluid average velocity
| :math:`A =` pipe area
| :math:`r =` pipe radius
| :math:`D =` pipe diameter


An example of changing flow geometries is when the a change in pipe size occurs in a circular piping system, as is demonstrated below. The flow through :math:`{\rm pipe} \, 1` must be the same as the flow through :math:`{\rm pipe} \, 2`.


    .. continuity_pipes:
    .. figure:: Images/continuity_pipes.png
        :width: 700px
        :align: center
        :alt: internal figure


Laminar and Turbulent Flow
---------------------------

Considering that this class deals with the flow of water through a water treatment plant, understanding the characteristics of the flow is very important. Thus, it is necessary to understand the most common characteristic of fluid flow: whether it is laminar or turbulent. `Laminar <https://en.wikipedia.org/wiki/Laminar_flow>`_ flow is very smooth and highly ordered. `Turbulent <https://en.wikipedia.org/wiki/Turbulence>`_ flow is chaotic, messy, and disordered. The best way to understand each flow and what it looks like is visually, `like in this video <https://youtu.be/qtvVN2qt968?t=131>`_ or the wikipedia image below. Please ignore the part of the video after the image of the tap.


    .. wikipedia_laminar_turbulent:
    .. figure:: Images/wikipedia_laminar_turbulent.png
        :width: 400px
        :align: center
        :alt: internal figure


A numeric way to determine whether flow is laminar or turbulent is by finding the `Reynolds number <https://en.wikipedia.org/wiki/Reynolds_number>`_, :math:`{\rm Re}`. The Reynolds number is a dimensionless parameter that compares inertia, represented by the average flow velocity :math:`\bar v` times a length scale :math:`D` to `viscosity <https://en.wikipedia.org/wiki/Viscosity>`_, represented by the kinematic viscosity :math:`\nu`. `Click here <https://www.youtube.com/watch?v=DVQw0svRHZA>`_ for a brief video explanation of viscosity. If the Reynolds number is less than 2,100 the flow is considered laminar. If it is more than a certain value, it is considered turbulent.

    .. math::

      {\rm Re = \frac{inertia}{viscosity}} = \frac{\bar vD}{\nu}

`There is a transition between laminar and turbulent flow which is not yet well understood <https://en.wikipedia.org/wiki/Laminar%E2%80%93turbulent_transition>`_. To simplify this phenomenon and make it possible to code for laminar or turbulent flow, we assume that the transition occurs at :math:`\rm{Re} = 2100`. The flow regime is assumed to be laminar below this value and turbulent above it. This variable is coded into aide_design as ``pc.RE_TRANSITION_PIPE``. We will neglect transitional flow.

Fluid can flow through very many different geometries like a pipe, a rectangular channel, or any other shape. To account for this, the characteristic length scale is quantified as the `hydraulic diameter <https://www.engineeringtoolbox.com/hydraulic-equivalent-diameter-d_458.html>`_, which can be applied to any geometry. For circular pipes, which are the most common geometry you’ll encounter in this class, the hydraulic diameter is simply the pipe diameter.

Here are other commonly used forms of the Reynolds number equation. They are the same as the one above, just with the substitutions :math:`Q = \bar v \frac{\pi D^2}{4}` and :math:`\nu = \frac{\mu}{\rho}`

    .. math::

      {\rm{Re}} = \frac{\bar vD}{\nu} = \frac{4Q}{\pi D\nu} = \frac{\rho \bar vD}{\mu}

| Such that:
| :math:`Q` = fluid flow rate in pipe
| :math:`D` = pipe diameter
| :math:`\bar v` = fluid velocity
| :math:`\nu` = fluid kinematic viscosity
| :math:`\mu` = fluid dynamic viscosity

.. seealso:: **Function in aide_design:** ``pc.re_pipe(FlowRate, Diam, Nu)`` Returns the Reynolds number *in a circular pipe*. Functions for finding the Reynolds number through other conduits and geometries can also be found in `physchem.py <https://github.com/AguaClara/aide_design/blob/master/aide_design/physchem.py>`_ within aide_design.

**Note:** Laminar and turbulent flow are described as two different
**flow regimes**. When there is a characteristic of flow and different
categories of the characteristic, each category is referred to as a flow
regime. For example, the Reynolds number describes a flow
characteristic, and its categories, referred to as flow regimes, are
laminar or turbulent.

Streamlines and Control Volumes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Both
`streamlines <https://en.wikipedia.org/wiki/Streamlines,_streaklines,_and_pathlines>`__
and **control volumes** are tools to compare different sections of a
system. For this class, this system will always be hydraulic.

Imagine water flowing through a pipe. A streamline is the path that a
particle would take if it could be placed in the fluid without changing
the original flow of the fluid. A more technical definition is “a line
which is everywhere parallel to the local velocity vector.”
Computational tools, `dyes (in
water) <https://proxy.duckduckgo.com/iur/?f=1&image_host=http%3A%2F%2Fwww.nuclear-power.net%2Fwp-content%2Fuploads%2F2016%2F05%2FFlow-Regime.png%3F4b884b&u=https://www.nuclear-power.net/wp-content/uploads/2016/05/Flow-Regime.png?4b884b>`__,
or `smoke (in
air) <https://www.youtube.com/watch?v=E9ZSAX56m0E&t=59s>`__ can be used
to visualize streamlines.

A control volume is just an imaginary 3-dimensional shape in space. Its
boundaries can be placed anywhere by the person applying the control
volume, and once set the boundaries remain fixed in space over time.
These boundaries are usually chosen to compare two relevant surfaces to
each other. The entirety of a control volume is usually not shown, as it
is often unnecessary. This is shown in the following image:

.. raw:: html

   <center>

.. raw:: html

   </center>

**Important Note:** Many images will be used over the course of this
class to show hydraulic systems. A standardized system of lines will be
used throughout them all to distinguish reference elevations from
control volumes from streamlines. This system is described in the image
below.

.. raw:: html

   <center>

.. raw:: html

   </center>

The Bernoulli and Energy Equations
----------------------------------

As explained in CEE 3310 with more details than most of you wanted to
know, the Bernoulli and energy equations are incredibly useful in
understanding the transfer of the fluid’s energy throughout a streamline
or through a control volume. The Bernoulli equation applies to two
different points along one streamline, whereas the energy equation
applies across a control volume. The energy of a fluid has three forms:
pressure, potential (deriving from elevation), and kinetic (deriving
from velocity).

The Bernoulli Equation
^^^^^^^^^^^^^^^^^^^^^^

These three forms of energy expressed above make up the Bernoulli
equation:

.. math:: \frac{p_1}{\rho g} + {z_1} + \frac{v_1^2}{2g} = \frac{p_2}{\rho g} + {z_2} + \frac{v_2^2}{2g}

| Such that:
| :math:`p` = pressure, :math:`\frac{[M]}{[L] \cdot [T]^2}`
| :math:`\rho` = fluid density, :math:`\frac{[M]}{[L]^3}`
| :math:`g` = acceleration due to gravity, :math:`\frac{[L]}{[T]^2}`, in
  aide_design as ``pc.gravity``
| :math:`z` = elevation relative to a reference, :math:`[L]`
| :math:`v` = fluid velocity, :math:`\frac{[L]}{[T]}`
| Where letters in brackets specify units:
| :math:`[M]` = mass
| :math:`[L]` = length
| :math:`[T]` = time

Notice that each term in this form of the Bernoulli equation has units
of :math:`[L]`, even though the terms represent the energy of water,
which has units of :math:`\frac{[M] \cdot [L]^2}{[T]^2}`. When energy of
water is described in units of length, the term used is called **head**.

There are two important distinctions to keep in mind when using head to
talk about energy. First is that head is dependent on the density of the
fluid under consideration. Take mercury, for example, which is around
13.6 times more dense than water. 1 meter of mercury head is therefore
equivalent to around 13.6 meters of water head. Second is that head is
independent of the amount of fluid being considered, *as long as all the
fluid is the same density*. Thus, raising 1 liter of water up by one
meter and raising 100 liters of water up by one meter are both
equivalent to giving the water 1 meter of water head, even though it
requires 100 times more energy to raise the hundred liters than to raise
the single liter. Since we are concerned mainly with water in this
class, we will refer to ‘water head’ simply as ‘head’.

Going back to the Bernoulli equation, the :math:`\frac{p}{\rho g}` term
is called the pressure head, :math:`z` the elevation head, and
:math:`\frac{v^2}{2g}` the velocity head. The following diagram shows
these various forms of head via a 1 meter deep bucket (left) and a jet
of water shooting out of the ground (right).

.. raw:: html

   <center>

.. raw:: html

   </center>

Assumption in using the Bernoulli equation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Though there are `many assumptions needed to confirm that the Bernoulli
equation can be
used <https://en.wikipedia.org/wiki/Bernoulli%27s_principle#Incompressible_flow_equation>`__,
the main one for the purpose of this class is that energy is not gained
or lost throughout the streamline being considered. If we consider more
precise fluid mechanics terminology, then “friction by viscous forces
must be negligible.” What this means is that the fluid along the
streamline being considered is not losing energy to viscosity. Energy
can only be transferred between its three forms if this equation is to
be used, it can’t be gained or lost.

Example problems
~~~~~~~~~~~~~~~~

`Here is a simple worksheet with very straightforward example problems
using the Bernoulli
equation. <https://www.teachengineering.org/content/cub_/lessons/cub_bernoulli/cub_bernoulli_lesson01_bepworksheetas_draft4_tedl_dwc.pdf>`__
Note that the solutions use the pressure-form of the Bernoulli equation.
This just means that every term in the equation is multiplied by
:math:`\rho g`, so the pressure term is just :math:`P`. The form of the
equation does not affect the solution to the problem it helps solved.

The Energy Equation
^^^^^^^^^^^^^^^^^^^

The assumption necessary to use the Bernoulli equation, which is stated
above, represents the key difference between the Bernoulli equation and
the energy equation for the purpose of this class. The energy equation
accounts for the (L)oss of energy from both the fluid flowing,
:math:`h_L`, and any other energy drain, like the charging of a
(T)urbine, :math:`h_T`. It also accounts for any energy inputs into the
system, :math:`h_P`, which is usually caused by a (P)ump within the
control volume.

.. math:: \frac{p_{1}}{\rho g} + z_{1} + \alpha_{1} \frac{\bar v_{1}^2}{2g} + h_P = \frac{p_{2}}{\rho g} + z_{2} + {\alpha_{2}} \frac{\bar v_{2}^2}{2g} + h_T + h_L

You’ll also notice the :math:`\alpha` term attached to the velocity
head. This is a correction factor for kinetic energy, and will be
neglected in this class. If you wish to learn more about the correction
factors, `click here to sate your
curiosity <http://nptel.ac.in/courses/105106114/pdfs/Unit6/6_1.pdf>`__.
In the Bernoulli equation, the velocity of the streamline of water is
considered, :math:`v`. The energy equation, however compares control
surfaces instead of streamlines, and the velocities across a control
surface many not all be the same. Hence, :math:`\bar v` is used to
represent the average velocity. Since AguaClara does not use pumps nor
turbines, :math:`h_P = h_T = 0`. With these simplifications, the energy
equation can be written as follows:

.. math:: \frac{p_{1}}{\rho g} + z_{1} + \frac{\bar v_{1}^2}{2g} = \frac{p_{2}}{\rho g} + z_{2} + \frac{\bar v_{2}^2}{2g} + h_L

**This is the form of the energy equation that you will see over and
over again in CEE 4540.** To summarize, the main difference between the
Bernoulli equation and the energy equation for the purposes of this
class is energy loss. The energy equation accounts for the fluid’s loss
of energy over time while the Bernoulli equation does not. So how can
the fluid lose energy?

Head Loss
---------

**Head (L)oss**, :math:`h_L` is a term that is ubiquitous in both this
class and fluid mechanics in general. Its definition is exactly as it
sounds: it refers to the loss of energy of a fluid as it flows through
space. There are two components to head loss: major losses caused by
pipe-fluid (f)riction, :math:`h_{\rm{f}}`, and minor losses caused by
fluid-fluid friction resulting from flow (e)xpansions, :math:`h_e`, such
that :math:`h_L = h_{\rm{f}} + h_e`.

Major Losses
^^^^^^^^^^^^

These losses are the result of friction between the fluid and the
surface over which the fluid is flowing. A force acting parallel to a
surface is referred to as
`shear <https://en.wikipedia.org/wiki/Shear_force>`__. It can therefore
be said that major losses are the result of shear between the fluid and
the surface it’s flowing over. To help in understanding major losses,
consider the following example: imagine, as you have so often in physics
class, pushing a large box across the ground. Friction is what resists
your efforts to push the box. The farther you push the box, the more
energy you expend pushing against friction. The same is true for water
moving through a pipe, where water is analogous to the box you want to
move, the pipe is similar to the floor that provides the friction, and
the major losses of the water through the pipe is analogous to the
energy **you** expend by pushing the box.

In this class, we will be dealing primarily with major losses in
circular pipes, as opposed to channels or pipes with other geometries.
Fortunately for us, Henry Darcy and Julius Weisbach came up with a handy
equation to determine the major losses in a circular pipe *under both
laminar and turbulent flow conditions*. Their equation is logically but
unoriginally named the `Darcy-Weisbach
equation <https://en.wikipedia.org/wiki/Darcy%E2%80%93Weisbach_equation>`__
and is shown below:

.. math:: h_{\rm{f}} \, = \, {\rm{f}} \frac{L}{D} \frac{\bar v^2}{2g}

Substituting the continuity equation :math:`Q = \bar vA` in the form of
:math:`\bar v^2 = \frac{16Q^2}{\pi^2 D^4}` gives another, equivalent
form of Darcy-Weisbach which uses flow, :math:`Q`, instead of velocity,
:math:`\bar v`:

.. math:: h_{\rm{f}} \, = \,{\rm{f}} \frac{8}{g \pi^2} \frac{LQ^2}{D^5}

| Such that:
| :math:`h_{\rm{f}}` = major loss, :math:`[L]`
| :math:`\rm{f}` = Darcy friction factor, dimensionless
| :math:`L` = pipe length, :math:`[L]`
| :math:`Q` = pipe flow rate, :math:`\frac{[L]^3}{[T]}`
| :math:`D` = pipe diameter, :math:`[L]`

**Function in aide_design:**
``pc.headloss_fric(FlowRate, Diam, Length, Nu, PipeRough)`` Returns only
major losses. Works for both laminar and turbulent flow.

Darcy-Weisbach is wonderful because it applies to both laminar and
turbulent flow regimes and contains relatively easy to measure
variables. The one exception is the Darcy friction factor,
:math:`\rm{f}`. This parameter is an approximation for the magnitude of
friction between the pipe walls and the fluid, and its value changes
depending on the whether or not the flow is laminar or turbulent, and
varies with the Reynolds number in both flow regimes.

For laminar flow, the friction factor can be determined from the
following equation:

.. math:: {\rm{f}} = \frac{64}{\rm{Re}}

For turbulent flow, the friction factor is more difficult to determine.
In this class, we will use the `Swamee-Jain
equation <https://en.wikipedia.org/wiki/Darcy_friction_factor_formulae#Swamee%E2%80%93Jain_equation>`__:

.. math:: {\rm{f}} = \frac{0.25} {\left[ \log \left( \frac{\epsilon }{3.7D} + \frac{5.74}{{\rm Re}^{0.9}} \right) \right]^2}

| Such that:
| :math:`\epsilon` = pipe roughness, :math:`[L]`
| :math:`D` = pipe diameter, :math:`[L]`

**Function in aide_design:** ``pc.fric(FlowRate, Diam, Nu, PipeRough)``
Returns :math:`\rm{f}` for laminar *or* turbulent flow. For laminar
flow, use ‘0’ for the ``PipeRough`` input.

The simplicity of the equation for :math:`\rm{f}` during laminar flow
allows for substitutions to create a very useful, simplified equation
for major losses during laminar flow. This simplification combines the
Darcy-Weisbach equation, the equation for the Darcy friction factor
during laminar flow, and the Reynold’s number formula:

.. math:: h_{\rm{f}} \, = \,{\rm{f}} \frac{8}{g \pi^2} \frac{LQ^2}{D^5}

.. math:: {\rm{f}} = \frac{64}{\rm{Re}}

.. math:: {\rm{Re}}=\frac{4Q}{\pi D\nu}

To form the `Hagen-Poiseuille
equation <https://en.wikipedia.org/wiki/Hagen%E2%80%93Poiseuille_equation>`__
for major losses during laminar flow, and *only* during laminar flow:

.. math:: h_{\rm{f}} = \frac{128\mu L Q}{\rho g\pi D^4}

.. math:: h_{\rm{f}} = \frac{32\nu L\bar v}{ g D^2}

The significance of this equation lies in its relationship between
:math:`h_{\rm{f}}` and :math:`Q`. Hagen-Poiseuille shows that the terms
are directly proportional (:math:`h_{\rm{f}} \propto Q`) during laminar
flow, while Darcy-Weisbach shows that :math:`h_{\rm{f}}` grows with the
square of :math:`Q` during turbulent flow
(:math:`h_{\rm{f}} \propto Q^2`). As you will soon see, minor losses,
:math:`h_e`, will grow with the square of :math:`Q` in both laminar and
turbulent flow. This has implications that will be discussed later, in
the flow control section.

In 1944, Lewis Ferry Moody plotted a ridiculous amount of experimental
data, gathered by many people, on the Darcy-Weisbach friction factor to
create what we now call the `Moody
diagram <https://en.wikipedia.org/wiki/Moody_chart>`__. This diagram has
the friction factor :math:`\rm{f}` on the left-hand y-axis, relative
pipe roughness :math:`\frac{\epsilon}{D}` on the right-hand y-axis, and
Reynolds number :math:`\rm{Re}` on the x-axis. The Moody diagram is an
alternative to computational methods for finding :math:`\rm{f}`.

.. raw:: html

   <center>

.. raw:: html

   </center>

Minor Losses
^^^^^^^^^^^^

Unfortunately, there is no simple ‘pushing a box across the ground’
example to explain minor losses. So instead, consider a `hydraulic
jump <https://www.youtube.com/watch?v=5spXXZX55C8>`__. In the video, you
can see lots of turbulence and eddies in the transition region between
the fast, shallow flow and the slow, deep flow. The high amount of
mixing of the water in the transition region of the hydraulic jump
results in significant friction *between water and water* (recall that
the measure of a fluid’s resistance to internal, fluid-fluid friction is
called **viscosity**). This turbulent, eddy-induced, fluid-fluid
friction results in minor losses, much like fluid-pipe friction results
in major losses.

As is the case in a hydraulic jump, a flow expansion (from shallow flow
to deep flow) creates the turbulent eddies that result in minor losses.
This will be a recurring theme in throughout the course: **minor losses
are caused by flow expansions**. Imagine a pipe fitting that connects a
small diameter pipe to a large diameter one, as shown in the image
below. The flow must expand to fill up the entire large diameter pipe.
This expansion creates turbulent eddies near the union between the small
and large pipes, and these eddies cause minor losses. You may already
know the equation for minor losses, but understanding where it comes
from is very important for effective AguaClara plant design. For this
reason, you are strongly recommended to read through the full
derivation, which can be found
`here <https://github.com/AguaClara/Textbook/blob/master/AguaClara%20Water%20Treatment%20Plant%20Design/Fluids%20Review/Fluids_Review_Derivations.md>`__.

There are three forms of the minor loss equation that you will see in
this class:

.. math::  {\rm{ \mathbf{First \, form:} }} \,\,\, h_e = \frac{\left( \bar v_{in}  - \bar v_{out} \right)^2}{2g}

.. math::  {\rm{ \mathbf{Second \, form:} }} \,\,\, h_e = \frac{\bar v_{in}^2}{2g}{\left( {1 - \frac{A_{in}}{A_{out}}} \right)^2} = \,\,\, \frac{\bar v_{in}^2}{2g} \mathbf{K_e^{'}}

.. math::  {\rm{ \mathbf{Third \, form:} }} \,\,\, h_e = \frac{\bar v_{out}^2}{2g}{\left( {\frac{A_{out}}{A_{in}}} -1 \right)^2} = \,\,\,\, \frac{\bar v_{out}^2}{2g} \mathbf{K_e}

| Such that:
| :math:`K_e^{'}, \,\, K_e` = minor loss coefficients, dimensionless

| **Function in aide_design:**
| ``pc.headloss_exp_general(Vel, KMinor)`` Returns :math:`h_e`. Can be
  either the second or third form due to user input of both velocity and
  minor loss coefficient. It is up to the user to use consistent
  :math:`\bar v` and :math:`K_e`.
| ``pc.headloss_exp(FlowRate, Diam, KMinor)`` Returns :math:`h_e`. Uses
  third form, :math:`K_e`.

**Note:** You will often see :math:`K_e^{'}` and :math:`K_e` used
without the :math:`e` subscript, they will appear as :math:`K^{'}` and
:math:`K`.

The :math:`in` and :math:`out` subscripts in each of the three forms
refer to the diagram that was used for the derivation:

.. raw:: html

   <center>

.. raw:: html

   </center>

The second and third forms are the ones which you are probably most
familiar with. The distinction between them, however, is critical.
First, consider the magnitudes of :math:`A_{in}` and :math:`A_{out}`.
:math:`A_{in}` can never be larger than :math:`A_{out}`, because the
flow is expanding. When flow expands, the cross-sectional area it flows
through must increase. As a result, both
:math:`\frac{A_{out}}{A_{in}} > 1` and
:math:`\frac{A_{in}}{A_{out}} < 1` must always be true. This means that
:math:`K^{'}` can never be greater than 1, while :math:`K` technically
has no upper limit.

If you have taken CEE 3310, you have seen tables of minor loss
coefficients `like this
one <https://www.engineeringtoolbox.com/minor-loss-coefficients-pipes-d_626.html>`__,
and they almost all have coefficients greater than 1. This implies that
these tables use the third form of the minor loss equation as we have
defined it, where the velocity is :math:`\bar v_{out}`. There is a good
reason for using the third form over the second one:
:math:`\bar v_{out}` is far easier to determine than
:math:`\bar v_{in}`. Consider flow through a pipe elbow, as shown in the
image below.

.. raw:: html

   <center>

.. raw:: html

   </center>

In order to find :math:`\bar v_{out}`, we first need to know which point
is :math:`out` and which point is :math:`in`. A simple way to
distinguish the two points is that :math:`in` occurs when the flow is
most contracted, and :math:`out` occurs when the flow has fully expanded
after that maximal contraction. Going on these guidelines, point ‘B’
above would be :math:`in`, since it represents the most contracted flow
in the elbow-pipe system. Therefore point ‘C’ would be :math:`out`, as
it is the point where the flow has fully expanded after its compression
in ‘B.’

:math:`\bar v_{out}` is easy to determine because it is the velocity of
the fluid as it flows through the entire area of the pipe. Thus,
:math:`\bar v_{out}` can be found with the continuity equation, since
the flow through the pipe and its diameter are easy to measure,
:math:`\bar v_{out} = \frac{4 Q}{\pi D^2}`. On the other hand,
:math:`\bar v_{in}` is difficult to find, as the area of the contracted
flow is dependent on the exact geometry of the elbow. This is why the
third form of the minor loss equation, as we have defined it, is the
most common.

Head Loss = Elevation Difference Trick
--------------------------------------

This trick, also called the ‘control volume trick,’ or more
colloquially, the ‘head loss trick,’ is incredibly useful for
simplifying hydraulic systems and is used all the time in this class.

Consider the following image, which was taken from the Flow Control and
Measurement powerpoint.

.. raw:: html

   <center>

.. raw:: html

   </center>

In systems like this, where an elevation difference is causing the flow
of water, the elevation difference is called the **driving head**. In
the system above, the driving head is the elevation difference between
the water level and the end of the tubing. Usually driving head is
written as :math:`\Delta z` or :math:`\Delta h`, though above it is
labelled as :math:`h_L`.

This image is violating the energy equation by saying that the elevation
difference between the water in the tank and the end of the tube is
:math:`h_L`. It implies that all of the driving head, :math:`\Delta z`,
is lost to head loss and therefore that no water is flowing out of the
tubing, which is not true. Let’s apply the energy equation between the
two red points. Pressures are atmospheric at both points and the
velocity of water at the top of tank is negligible.

.. math:: \rlap{\Bigg/}\frac{p_{1}}{\rho g} + z_{1} + \rlap{\Bigg/}\frac{\bar v_{1}^2}{2g} = \rlap{\Bigg/}\frac{p_{2}}{\rho g} + z_{2} + \frac{\bar v_{2}^2}{2g} + h_L

We now get:

.. math:: \Delta z = \frac{\bar v_2^2}{2g} + h_L

This contradicts the image above, which says that :math:`\Delta z = h_L`
and neglects :math:`\frac{\bar v_2^2}{2g}`. The image above is correct,
however, if you apply the head loss trick. The trick incorporates the
:math:`\frac{\bar v_2^2}{2g}` term *into* the :math:`h_L` term as a
minor loss. See the math below:

.. math:: \Delta z = \frac{\bar v_2^2}{2g} + h_e + h_f

.. math:: \Delta z = \frac{\bar v_2^2}{2g} + \left( \sum K \right) \frac{\bar v_2^2}{2g} + h_f

.. math:: \Delta z = \left( 1 + \sum K \right) \frac{\bar v_2^2}{2g} + h_f

This last step incorporated the kinetic energy term of the energy
equation, :math:`\frac{\bar v_2^2}{2g}`, into the minor loss equation by
saying that its :math:`K` is 1. From here, we reverse our steps to get
:math:`\Delta z = h_L`

.. math:: \Delta z = h_e + h_f

.. math:: \Delta z = h_L

By applying the head loss trick, you are considering the entire flow of
water out of a control volume as lost energy. This is just an algebraic
trick, the only thing to remember when applying this trick is that
:math:`\sum K` will always be at least 1, even if there are no ‘real’
minor losses in the system.

The Orifice Equation
--------------------

This equation is one that you’ll see again and again throughout this
class. Understanding it now will be invaluable, as future concepts will
use and build on this equation.

Vena Contracta
^^^^^^^^^^^^^^

Before describing the equation, we must first understand the concept of
a `vena contracta <https://en.wikipedia.org/wiki/Vena_contracta>`__.
Refer once more to this image of flow through a pipe elbow.

.. raw:: html

   <center>

.. raw:: html

   </center>

The flow contracts as the fluid moves from point ‘A’ to point ‘B.’ This
happens because the fluid can’t make a sharp turn at the corner of the
elbow. Instead, the streamline closest to the sharp turn makes a slow,
gradual change in direction, as shown in the image. As a result of this
gradual turn, the cross-sectional area the fluid is flowing through at
point ‘B’ is less than the cross-sectional area it flows through at
points ‘A’ and ‘C’. Written as an equation,
:math:`A_{csB} < A_{csA} = A_{csC}`, where the :math:`_{csA}` stands for
‘control surface :math:`A`’ subscript

The term ‘vena contracta’ describes the phenomenon of contracting flow
due to streamlines being unable to make sharp turns. :math:`\Pi_{vc}` is
a ratio between the flow area at the vena contracta, :math:`A_{csB}`,
which is when the flow is *maximally* contracted, and the flow area
*before* the contraction, :math:`A_{csA}`. In the image above, the
equation for the vena contracta coefficient would be:

.. math:: \Pi_{vc} = \frac{A_{csB}}{A_{csA}}

Note that what this class calls :math:`\Pi_{vc}` is often referred to as
a ‘Coefficient of Contraction,’ :math:`C_c`, in other engineering
courses and settings. When the most extreme turn a streamline must make
is 90°, the value of the vena contracta coefficient is close to 0.62.
This parameter is in aide_design as ``pc.RATIO_VC_ORIFICE``. The vena
contracta coefficient value is a function of the flow geometry.

**A vena contracta coefficient is not a minor loss coefficient.** Though
the equations for the two both involve contracted and non-contracted
areas, these coefficients are not the same. Refer to the flow through a
pipe elbow image above. The minor loss coefficient equation uses the
areas of points ‘B’ and ‘C,’ while the vena contracta coefficient uses
the areas of points ‘A’ and ‘B.’ Additionally, the equations to
calculate the coefficients themselves are not the same. Confusing the
two coefficients is common mistake that this paragraph will hopefully
help you to avoid.

Origin
^^^^^^

The orifice equation is derived from the Bernoulli equation as applied
to the red points in the following image:

.. raw:: html

   <center>

.. raw:: html

   </center>

At point A, the pressure is atmospheric and the instantaneous velocity
is negligible as the water level in the bucket drops slowly. At point B,
the pressure is also atmospheric. We define the difference in elevations
between the two points, :math:`z_A - z_B`, to be :math:`\Delta h`. With
these simplifications (:math:`p_A = \bar v_A = p_B = 0`) and assumptions
(:math:`z_A - z_B = \Delta h`), the Bernoulli equation becomes:

.. math:: \Delta h = \frac{\bar v_B^2}{2g}

Substituting the continuity equation :math:`Q = \bar v A` in the form of
:math:`\bar v_B^2 = \frac{Q^2}{A_{vc}^2}`, the vena contracta
coefficient in the form of :math:`A_{vc} = \Pi_{vc} A_{or}` yields:

.. math:: \Delta h = \frac{Q^2}{2g \Pi_{vc}^2 A_{or}^2}

Which, rearranged to solve for Q gives **The Orifice Equation:**

.. math:: Q = \Pi_{vc} A_{or} \sqrt{2g\Delta h}

| Such that:
| :math:`\Pi_{vc}` = 0.62 = vena contracta coefficient, in aide_design
  as ``pc.RATIO_VC_ORIFICE``
| :math:`A_{or}` = orifice area- NOT contracted flow area
| :math:`\Delta h` = elevation difference between orifice and water
  level

| **Equations in aide_design:**
| ``pc.flow_orifice(Diam, Height, RatioVCOrifice)`` Returns flow through
  a horizontal orifice.
| ``pc.flow_orifice_vert(Diam, Height, RatioVCOrifice)`` Returns flow
  through a vertical orifice. The height parameter refers to height
  above the center of the orifice.

.. raw:: html

   <center>

.. raw:: html

   </center>

There are two configurations for an orifice in the wall of a reservoir
of water, horizontal and vertical, as the image above shows. The orifice
equation shown in the previous section is for a horizontal orifice, but
for a vertical orifice the equation requires integration to return the
correct flow. You will explore this in the Flow Control and Measurement
Design Challenge.

Section Summary
---------------

1. **Bernoulli vs energy equations:** The Bernoulli equation assumes
   that energy is conserved throughout a streamline or control volume.
   The Energy equation assumes that there is energy loss, or head loss
   :math:`h_L`. This head loss is composed of major losses,
   :math:`h_{\rm{f}}`, and minor losses, :math:`h_e`.

Bernoulli equation:

.. math:: \frac{p_1}{\rho g} + {z_1} + \frac{\bar v_1^2}{2g} = \frac{p_2}{\rho g} + {z_2} + \frac{\bar v_2^2}{2g}

Energy equation, simplified to remove pumps, turbines, and
:math:`\alpha` factors:

.. math:: \frac{p_{1}}{\rho g} + z_{1} + \frac{\bar v_{1}^2}{2g} = \frac{p_{2}}{\rho g} + z_{2} + \frac{\bar v_{2}^2}{2g} + h_L

2. **Major losses:** Defined as the energy loss due to shear between the
   walls of the pipe/flow conduit and the fluid. The Darcy-Weisbach
   equation is used to find major losses in both laminar and turbulent
   flow regimes. The equation for finding the Darcy friction factor,
   :math:`\rm{f}`, changes depending on whether the flow is laminar or
   turbulent. The Moody diagram is a common graphical method for finding
   :math:`\rm{f}`. During laminar flow, the Hagen-Poiseuille equation,
   which is just a combination of Darcy-Weisbach, Reynolds number, and
   :math:`{\rm{f}} = \frac{64}{\rm{Re}}`, can be used

| Darcy-Weisbach equation:
|

.. math:: h_{\rm{f}} = {\rm{f}} \frac{L}{D} \frac{\bar v^2}{2g}

For water treatment plant design we tend to use plant flow rate, :math:`Q`, as our master variable and thus we have.

.. math:: h_{\rm{f}} = {\rm{f}} \frac{8}{g \pi^2} \frac{LQ^2}{D^5}

:math:`\rm{f}` for laminar flow:

.. math:: {\rm{f}} = \frac{64}{\rm{Re}} = \frac{16 \pi D \nu}{Q} = \frac{64 \nu}{\bar v D}

:math:`\rm{f}` for turbulent flow:

.. math:: {\rm{f}} = \frac{0.25} {\left[ \log \left( \frac{\epsilon }{3.7D} + \frac{5.74}{{\rm Re}^{0.9}} \right) \right]^2}

Hagen-Poiseuille equation for laminar flow:

.. math:: h_{\rm{f}} = \frac{32\mu L \bar v}{\rho gD^2} = \frac{128\mu Q}{\rho g\pi D^4}

3. **Minor losses:** Defined as the energy loss due to the generation of
   turbulent eddies when flow expands. Once more: minor losses are
   caused by flow expansions. There are three forms of the minor loss
   equation, two of which look the same but use different coefficients
   (:math:`K^{'}` vs :math:`K`) and velocities (:math:`\bar v_{in}` vs
   :math:`\bar v_{out}`). *Make sure the coefficient you select is
   consistent with the velocity you use*.

First form:

.. math:: h_e = \frac{\left( \bar v_{in}  - \bar v_{out} \right)^2}{2g}

Second form:

.. math:: h_e = \frac{\bar v_{in}^2}{2g}{\left( {1 - \frac{A_{in}}{A_{out}}} \right)^2} = \,\,\, \frac{\bar v_{in}^2}{2g} \mathbf{K^{'}}

Third and most common form:

.. math:: h_e = \frac{\bar v_{out}^2}{2g}{\left( {\frac{A_{out}}{A_{in}}} -1 \right)^2} = \,\,\,\, \frac{\bar v_{out}^2}{2g} \mathbf{K}

4. **Major and minor losses vary with flow:** While it is generally
   important to know how increasing or decreasing flow will affect head
   loss, it is even more important for this class to understand exactly
   how flow will affect head loss. As the table below shows, head loss
   will always be proportional to flow squared during turbulent flow.
   During laminar flow, however, the exponent on :math:`Q` will be
   between 1 and 2 depending on the proportion of major to minor losses.

+------------------------+--------------+--------------+
| Head loss scales with: | Major Losses | Minor Losses |
+========================+==============+==============+
| Laminar                | :math:`Q`    | :math:`Q^2`  |
+------------------------+--------------+--------------+
| Turbulent              | :math:`Q^2`  | :math:`Q^2`  |
+------------------------+--------------+--------------+

5. The **head loss trick**, also called the control volume trick, can be
   used to incorporate the ‘kinetic energy out’ term of the energy
   equation, :math:`\frac{\bar v_2^2}{2g}`, into head loss as a minor
   loss with :math:`K = 1`, so the minor loss equation becomes
   :math:`\left( 1 + \sum K \right) \frac{\bar v^2}{2g}`. This is used
   to be able to say that :math:`\Delta z = h_L` and makes many equation
   simplifications possible in the future.

6. **Orifice equation and vena contractas:** The orifice equation is
   used to determine the flow out of an orifice given the elevation of
   water above the orifice. This equation introduces the concept of a
   vena contracta, which describes flow contraction due to the inability
   of streamlines to make sharp turns. The equation shows that the flow
   out of an orifice is proportional to the square root of the driving
   head, :math:`Q \propto \sqrt{\Delta h}`. Depending on the orientation
   of the orifice, vertical (like a hole in the side of a bucket) or
   horizontal (like a hole in the bottom of a bucket), a different
   equation in aide_design should be used.

The Orifice Equation:

.. math:: Q = \Pi_{vc} A_{or} \sqrt{2g\Delta h}
