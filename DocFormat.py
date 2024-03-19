from typing import Any


class DocFormat:
    def __init__(self, name = '', title = '', className = '', Lab=True):
        self.__name = name
        self.__title = title
        self.__Lab = Lab
        self.__questions = {}
        self.__questionsB = {}
        self.__className = className
        self.__doc = ''

     ### SETTERS
    
    def set_name(self, name: str) -> None:
        self.__name = name
    
    def set_title(self, title: str) -> None:
        self.__title = title
    
    def set_lab(self, lab: bool) -> None:
        self.__Lab = lab
    
    def set_className(self, className: str) -> None:
        self.__className = className

    def set_questions(self, questions: dict = {}) -> None:
        self.__questions = questions

    def set_questionsPartB(self, questionsB: dict = {}) -> None:
        self.__questionsB = questionsB

    def custom_doc(self, doc: str) -> None:
        self.__doc = doc

    def islab(self):
        return self.__Lab #returns true if lab, false if homework
    
    ### METHODS
    

    def create_formatting_beginning(self) -> str:

        out = r"""
\documentclass[12pt,reqno]{article}
\usepackage{listings,xcolor, xcolor, graphicx}
\usepackage[margin=.5in]{geometry}
\usepackage[labelformat=empty]{caption}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.93,0.92,0.95}

\lstdefinestyle{myStyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}

\title{\Huge{"""+ str(self.__title) + r"""}
    \\
\Large\scshape{"""+ str(self.__className) + r"""}}
\author{"""+ str(self.__name) + r"""}
\date{\today}

\lstset{style=myStyle}
\begin{document}

\maketitle
\begin{enumerate}
"""
        return out
    
    def create_formatting_end(self) -> str:
        out = '\n'
        out = r"""
\end{enumerate}
\end{document}
"""
        return out

    def hw_entry(self):
        
        ans = self.__questions
        rStr = r"""
    \section{Part A}
    """
        for question in self.__questions:
            rStr += r"""
    \item """ + question + r"""
    \begin{lstlisting}[language=C]
""" + self.__questions[question] + r"""
    \end{lstlisting}
"""
        for question in self.__questionsB:
            rStr += r"""
    \section{Part B}
    \item """ + question + r"""
    \begin{figure}[h]
    %\includegraphics[width=\linewidth]{""" + self.__questionsB[question] + r"""}

    \end{figure}
    \newpage 
"""
        return rStr
    

    def lab_entry(self ):
        for question in self.__questions:
            rStr = r"""
    \item """ + question + r""" 
    \begin{figure}[h]
        \includegraphics[width=.95\linewidth]{""" + self.__questions[question] + r"""}
        
    \end{figure}
    \newpage 


"""
        return rStr

    def buildFormat(self):
        rstr = self.create_formatting_beginning()

        match self.__Lab:
            case True:
                rstr += self.lab_entry()
            case False:
                rstr += self.hw_entry()
            case _:
                raise Exception("Invalid Lab or Homework")
    
        rstr += self.create_formatting_end()

        self.__doc = rstr



    def __str__(self) -> str:
        return self.__doc
    

if __name__ == "__main__":
    print("This is the formattingHelpers class")
    
    doc = DocFormat()
    doc.set_name("Ryan")
    doc.set_title("Homework 3")
    doc.set_className("ENGR 213")
    doc.set_lab(False)
    qA = {'Question 1': 'ans','Question 2': 'ans2'}
    qB = {'Question 1': 'ans','Question 2': 'ans2'}
    doc.set_questions(qA)
    doc.set_questionsPartB(qB)
    doc.buildFormat()
    print(doc)