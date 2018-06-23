.. _example_aguaclara_rst:

================================
Example AguaClara RST
================================

* Always have a clear, informative title, as seen above.
* For headings, use the following:
  + # with overline, for parts
  + * with overline, for chapters
  + =, for sections
  + -, for subsections
  + ^, for subsubsections
  + “, for paragraphs

* When writing code, :code:`use an inline code block` or a

    .. code::

      code block

* Figures...
    .. figure:: https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg
        :width: 200px
        :align: center
        :height: 100px
        :alt: alternate text

        always need captions and alt-text.

* Math is very cool, and works natively in rst:

  .. math::
     :nowrap:

     \begin{eqnarray}
        y    & = & ax^2 + bx + c \\
        f(x) & = & x^2 + 2xy + y^2
     \end{eqnarray}

  .. math::

     n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

* Tables should be made using csv pasted in:

  .. csv-table:: a title
   :header: "name", "firstname", "age"
   :widths: 20, 20, 10

   "Smith", "John", 40
   "Smith", "John, Junior", 20
* last bullet
