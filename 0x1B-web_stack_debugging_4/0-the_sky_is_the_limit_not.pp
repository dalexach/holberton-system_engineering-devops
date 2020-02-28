# Changing the ngnix config to repare requests
exec { 'Increase_workers':
    command  => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/ngnix.cof && sudo service nginx restart",
    provider => 'shell',
}
