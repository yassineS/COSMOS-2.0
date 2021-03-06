.. _introduction:

Introduction
============
`COSMOS <http://cosmos.hms.harvard.edu>`_ is a Python library for workflow management that allows formal description of pipelines and partitioning of jobs. In addition, it includes a user-interface for tracking the progress of jobs, abstraction of the queuing system and fine-grained control over the workflow. Workflows can be created on traditional computing clusters as well as cloud-based services. It is developed jointly by the `Laboratory for Personalized Medicine <http://lpm.hms.harvard.edu/>`_ at Harvard Medical School and the `Wall Lab <wall-lab.stanford.edu>`_ at Stanford University.

COSMOS allows you to efficiently program complex workflows of command line tools that automatically take
advantage of a compute cluster, and provides a web dashboard to monitor, debug, and analyze your jobs.  Cosmos is
able to scale on a traditional cluster such as :term:`LSF` or :term:`SGE` with a shared filesystem.  It is especially
powerful when combined with spot instances on `Amazon Web Services <aws.amazon.com>`_ and
`StarCluster <http://star.mit.edu/cluster/>`_.

Cite COSMOS
___________

Gafni E, Luquette LJ, Lancaster AK, Hawkins JB, Jung J-Y, Souilmi Y, Wall DP, Tonellato PJ: COSMOS: Python library for massively parallel workflows. Bioinformatics 2014. doi: `10.1093/bioinformatics/btu385 <http://bioinformatics.oxfordjournals.org/content/30/20/2956>`_.

History
___________

Since the original publication, COSMOS has been re-written and open-sourced by the original author, in a collaboration between
`The Laboratory for Personalized Medicine <http://lpm.hms.harvard.edu/>`_ at Harvard Medical School, the `Wall Lab <http://wall-lab.stanford.edu/>`_ at Stanford University, and
`Invitae <http://invitae.com>`_, a clinical genetic sequencing diagnostics laboratory.

Features
_________

* Powerful syntax for the creation of complex and highly parallelized workflows.
* Reusable recipes and definitions of tools and sub-workflows allows for DRY code.
* Keeps track of workflows, job information, and resource utilization and provenance in an SQL database.
* The ability to visualize all jobs and job dependencies as a convenient image.
* Monitor and debug running workflows, and a history of all workflows via a web dashboard.
* Alter and resume failed workflows.

Multi-platform Support
+++++++++++++++++++++++

* Support for :term:`DRMS` such as SGE, LSF.  :term:`DRMAA` coming soon.  Adding support for more DRMs is very straightforward.
* Supports for MySQL, PosgreSQL, Oracle, SQLite by using the :term:`Sqlalchemy` ORM.
* Extremely well suited for cloud computing, especially when used in conjuection with `AWS <http://aws.amazon.com>`_ and `StarCluster <http://star.mit.edu/cluster/>`_.
