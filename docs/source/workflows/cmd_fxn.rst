.. _tools:

.. py:module:: cosmos.core

Core
==================

A `command_fxn` (or `cmd_fxn`) represents a command-line tool (like echo, cat, paste, or a custom script).  It returns a String,
which gets written to the filesystem as a shell-script and submitted as a job.  It is a plain old python function.

.. code-block:: python

    from cosmos.api import find, out_dir

    def word_count(use_lines=False, in_txt=find('txt$'), out_txt=out_dir('count.txt')):
        l = ' -l' if use_lines else ''
        return r"""
            wc{l} {in_txt} > {out_txt}
            """.format(**locals())

    word_count(True, '/path/to/input_file.txt', 'output_count.txt')
    >>> "wc -l /path/to/input_file.txt output_count.txt"

There are some special things about `cmd_fxn` parameters that Cosmos will recognize.

* A function parameter that starts with `in_` is an input_file.
* A function parameter that starts with `out_` is an output_file.
* The :func:`find` default can be specified for input files (and almost always is).  This will cause Cosmos, by default,
  to search all of the parents of a Task for files that match the find's :param:`regex` parameter.
* :func:`out_dir` will automatically append the Task's output directory to the filename.
* :func:`forward` will automatically set an output_file to the input_file specified.


More on find()
--------------

The cardinality (The `n` parameter), is enforced such that ``n`` number of input_files should match.  By default,
the cardinality of each abstract_input_file is ``==1``, but this can be changed using the ``n`` parameter: ie ``find(format='txt', n='>=1')``.
If you specify a cardinality where there may be more than 1, for example ``n='>=1'``, the value passed into this input_file
will be a list of file paths, rather than a string (even if only 1 match was found).  All basic operations work,
for example:

* "==2"
* "<3"
* ">=4"

``find()`` can also be passed a dict of ``tags``, which will filter the search space of parents to Task's who's ``tags``

You can always explicitly specify input_files via tags, should find() not work for you.

API
-----------


Command Function I/O
+++++++++++++++++++++
.. autofunction:: cosmos.api.find

.. autofunction:: cosmos.api.out_dir

.. autofunction:: cosmos.api.forward