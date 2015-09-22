## ncbk

Ncbk's a very basic helper that uses [Plan](http://plan.readthedocs.org/index.html) to run cronjobs
in a simpler manner - in this case, the goal is to have daily Redis dumps for [notCRUD](https://github.com/wingify/notcrud). 

As of now, all ncbk does is control the cronjob that uses Redis' ```BGSAVE``` command to create 
an AOF + RDF dump containing all of notCRUD's keys. In a bit, this will support backing up
these dumps to S3 or some such object store, as well as have multiple backups over multiple time
periods.