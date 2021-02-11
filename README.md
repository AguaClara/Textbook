# Textbook [![Documentation](https://github.com/AguaClara/Textbook/workflows/Documentation/badge.svg)](https://aguaclara.github.io/Textbook/)

Please enjoy [the AguaClara textbook](https://aguaclara.github.io/Textbook/)!  
If you are interested in helping out by writing, begin by reading [this page](https://github.com/AguaClara/Textbook/wiki/Contributing-by-writing)!  
If you are interested in helping out by editing existing sections, begin by reading [this page](https://github.com/AguaClara/Textbook/wiki/Contributing-by-editing)!

# Textbook Structure
This is the first version attempted of an AguaClara textbook. The current proposed structure is as follows:

Each chapter will cover a unit process, like "Flow Control and Measurement" or "Sedimentation."

Each chapter will have the following three sections:
- Introduction
- Design
- Theory and Future Work

Each chapter may also have up to three appendices:
- Appendix A: Derivations
- Appendix B: Examples


## Introduction
The introduction contains two components:
- Introduces and explains concepts relevant to the physics and design of the unit process
- Covers briefly the design of conventional water treatment plants and how they solve the problems associated with the unit process.  

## Design
Contains the details of an AguaClara design for the unit process. Goes over logic and explains thoroughly why design decisions are made.

## Theory and Future Work
Contains working theories in the AguaClara lab and future research projects to better understand the physics of water treatment and improve plant design.

## Publishing

To publish, first ensure all of your changes have been merged into master by following the Pull Request best practices [here](https://github.com/AguaClara/Textbook/wiki/Contributing-by-writing). Then follow these steps:

1. `git checkout master`
2. `git pull`
3. `git tag <tagname>`
   1. To get `<tagname>`, check the latest release and increment by 1, following semantic versioning. For Example, if the current version were `v0.0.76` and there were only small edits the next would be `v0.0.77`. If there were more significant changes it would be `v0.1.0`, and for extremely large changes (maybe a whole new chapter?), `v1.0.0`.
4. `git push origin <tagname>`

Pushing a tag will kick off the automated release workflow which builds the PDF and HTML documentation.

## Appendix A: Derivations
Many of the equations that show up in the `Introduction` and `Design` sections have lengthy derivations that have been done by AguaClara in the past. The step-by-step derivations of these equations will be found in this section. Equations that require derivations will be noted as such in the text and linked to their derivations.


## Appendix B: Examples
This section will contain example problems. A big portion of these example problems will be design challenges that were used in previous years, before this textbook was made available.
