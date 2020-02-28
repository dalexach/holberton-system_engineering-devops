# Changing the ngnix config to repare requests
exec { 'Repare_requests':
    command  => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/ngnix.conf && sudo service nginx restart",
    provider => 'shell',
}
