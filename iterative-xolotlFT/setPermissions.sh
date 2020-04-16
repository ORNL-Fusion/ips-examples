#!/bin/bash
setfacl -R -m g:m1709:rwX `pwd`
find `pwd` -type d | xargs setfacl -R -m d:g:m1709:rwX
#chmod -R ug+rwX `pwd`
#chgrp -R atom `pwd`
#find `pwd` -type d -exec chmod g+s '{}' \;
