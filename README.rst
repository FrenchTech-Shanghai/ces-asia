###################################################
CES Asia - La French Tech Shanghai CES Asia website
###################################################

A website to support the initiative of La French Tech Shanghai to organise a French Tech startup corner at CES Asia.


Development
===========

To install the development environment, follow those steps:

.. code:: shell

    $ pip install requirements.txt
    $ nodeenv -p --prebuilt -c
    $ npm install -g bower
    $ bower install
    $ pybabel compile -d translations

Create database
---------------

.. code:: shell

    $ python utils/init_db.py

Compile requirement file
------------------------

.. code:: shell

    $ pip install pip-tools
    $ pip-compile requirements.in

i18n & translation
------------------

Make sure all the strings are passed through ``gettext()`` or ``_()`` in the python
files or the templates.

After adding new strings, run the following commands:

.. code-block:: sh

    $ pybabel extract -F babel.cfg -o messages.pot ces_asia/
    $ pybabel update -i messages.pot -d ces_asia/translations

You can now edit the ``.po`` files in the ``ces_asia/translations/`` folder. When the translations are done, run the following:

.. code-block:: sh

    $ pybabel compile -d ces_asia/translations

License
=======

The code in this project is under a BSD 3-clause license, see the 'LICENSE' file. All the artworks and non-code are under a Creative Commons by-nc 4.0 license, see http://creativecommons.org/licenses/by-nc/4.0/.
The name French Tech and the associated logos are copyrighted and licensed by BPIFrance.
