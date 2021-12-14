''' write a python programme to set the indentation'''
import textwrap
sample_text='''Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language'''
print(sample_text)
text1=textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))
print()