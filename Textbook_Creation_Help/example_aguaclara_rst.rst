.. _example_aguaclara_rst:

*****************************
Example AguaClara RST
*****************************

How to use this file:
=====================
Open the source code of the file next to the rendered code. The source code is
found by clicking "View page source" at the top of the page. Next, follow along with the
source code and rendered code. When you want to use the source code

* Always have a clear, informative title, as seen above.
* For headings, use the following
    + \* with overline, for sections
    + = for sections
    + -, for subsections
    + ^, for subsubsections
    + “, for subsubsubsections

* When writing code, :code:`use an inline code block` or a

    .. code::

      code block

* Figures...

    .. figure:: https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg
        :width: 200px
        :align: center
        :height: 100px
        :alt: external figure

        always need captions and alt-text. And this is an external (url) figure.

    .. _mountain:
    .. figure:: mountain.jpg
        :width: 300px
        :align: center
        :alt: internal figure

        Here is an internally referenced figure. Specify folders with folder/image.jpg


* Math is very cool, and works natively in rst:

  .. math::
     :label: quadratic

        y   = ax^2 + bx + c \\

  .. math::

     n_{\rm{offset}} = \sum_{k=0}^{N-1} s_k n_k

* Tables should be made using csv pasted in:

  .. _an_example_table:
  .. csv-table:: Example Table
   :header: "name", ":math:`\bar\varepsilon`", "age"
   :widths: 20, 20, 10

   "Smith", "John", 40
   "Smith", "John, Junior", 20

Is this normal?
:math:`\bar\varepsilon`

:math:`\begin{matrix}
 &\varepsilon  &\varepsilon  &\varepsilon \\
 &\varepsilon  &\varepsilon  &\varepsilon \\
 &\varepsilon  &\varepsilon  &\varepsilon
\end{matrix}``


* References work by referencing any "target." This can be a figure :numref:`mountain`, equation :eq:`quadratic`,
  or table :numref:`an_example_table`.
* Colored :red:`text`. Add colors/styles by using roles defined in /conf.py and /_static/css/custom.css.
