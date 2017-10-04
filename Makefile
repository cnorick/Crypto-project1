all:
	# Move executables to this directory and remove thier '.sh' suffix.
	cp bash_scripts/cbc-dec.sh cbc-dec
	cp bash_scripts/cbc-enc.sh cbc-enc
	cp bash_scripts/ctr-dec.sh ctr-dec
	cp bash_scripts/ctr-enc.sh ctr-enc

	# Change permission on files to allow execution
	chmod a+x cbc-dec
	chmod a+x cbc-enc
	chmod a+x ctr-dec
	chmod a+x ctr-enc

clean:
	rm cbc-enc cbc-dec ctr-enc ctr-dec