### Exercise 00: Innocent Prank
The new HTML file should be named "evilcorp_hacked.html" and placed in the same directory as the source
"evilcorp.html" file.

### Exercise 01: Cash Flow

After a while, Elliot turned his laptop on the table, showing the script. Mobley gave him a thumbs up and 
Trenton exchanged places with Darlene near the pinboard.

Using [Redis](https://redis.io/) pubsub as a queue broker.

Consumer should receive an argument with a list of account numbers like this:

`~$ python consumer.py -e 7134456234,3476371234`

where `-e` is a parameter receiving a list of bad guys' account numbers. When started, it should read
messages from a pubsub queue and print them to stdout on one line each. For accounts from the 
"bad guys' list" if they are specified as a receiver consumer should *swap* sender and receiver for
the transaction. But this should happend *only* in case "amount" is not negative.

For example, if producer generates three messages like these:

```
{"metadata": {"from": 1111111111,"to": 2222222222},"amount": 10000}
{"metadata": {"from": 3333333333,"to": 4444444444},"amount": -3000}
{"metadata": {"from": 2222222222,"to": 5555555555},"amount": 5000}
```

consumer started like `~$ python consumer.py -e 2222222222,4444444444` should print out:

```
{"metadata": {"from": 2222222222,"to": 1111111111},"amount": 10000}
{"metadata": {"from": 3333333333,"to": 4444444444},"amount": -3000}
{"metadata": {"from": 2222222222,"to": 5555555555},"amount": 5000}
```

Notice that only the first line was changed. Second one wasn't because "amount" was negative (even
though receiver is a bad guy). Third one wasn't changed because bad guy is a sender, not a receiver.


### Exercise 02: Deploy
These tasks should be generated in Ansible notation (e.g. look [here](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html) for notation
on copying files). The script should be named "gen_ansible.py".

Your code should convert "todo.yml" into "deploy.yml" following this notation.

### Reading and tips

Working with HTML is one of the typical tasks when you are writing parsers and various server 
code using Python. Two libraries that are most widely used for this are [lxml](https://lxml.de/) and 
aforementioned [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). They are not mutually exclusive,
though, as lxml can be used as a parsing backend for BS4, combining great performance with pretty
good API flexibility. You can read about parsing backends [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser).

Working with Redis is also a pretty common task to encounter in the world of applied Python. 
And it can also be optimized by using an optional [low-level C wrapper](https://github.com/redis/hiredis-py). It is not a necessary
requirement in this task, but still a good module to know about.

Working with YAML is also a very common task, for which [PyYAML](https://pyyaml.org/) is often used. Parsing config
files or writing Ansible plugins is something you can encounter often if Python is used in your 
team as a language for dealing with infrastructure. It would require a lot of time and text to
introduce a specific YAML format for this task, that's why an existing standard is chosen here.
Even though it requires a bit of time and effort to study, it can be really helpful to know the 
very basics of Ansible for your future job or just daily automation tasks.

By the way, just in case you're curious, Ansible [does support Windows](https://docs.ansible.com/ansible/latest/user_guide/windows_usage.html) as well!    
