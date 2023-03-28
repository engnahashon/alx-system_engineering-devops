# Create the SSH directory if it does not exist
file { '/root/.ssh':
  ensure => directory,
  mode   => '0700',
}

# Create or modify the SSH configuration file
file { '/root/.ssh/config':
  ensure  => file,
  mode    => '0600',
  owner   => 'root',
  group   => 'root',
  content => "Host myserver\n\
              Hostname 192.168.1.100\n\
              IdentityFile /root/.ssh/school\n\
              PreferredAuthentications publickey\n\
              PasswordAuthentication no\n",
}

# Add the public key to the remote server
ssh_authorized_key { 'my_key':
  user    => 'root',
  type    => 'ssh-rsa',
  key     => 'AAAAB3NzaC1yc2EAAAADAQABAAABAQC/gxwnB/Qd2w4NU4GnM4B+v9dLk37zR7YlY98l2QV3iENhrTnTg7+jZszziru9X+v/+zzzRJyM+l+obz2Q1VqOJ8k/S7VfMygOuN9BXoU6F58UXXyIY6+0UkVJv1iWw4Z4U0Zl18XKfXjhM5zBEr5JEdaa5hPnGGv+8WwJ1k48hLZn3+tzP6FrqP3yX9nBLx1M7aM8gH1Feh4AF4GikzTKoJl8pPHMYyHbxwoS9i2f81c1ewJdZPdhrZwIfFnl8DTvxbDQX9r5rM1HcW8jv5P5pepBcZlYqG68ltAkL75wtzRkJ1RdDpyiheW8yxvVTb7Iu6cymTQZzU6b0U6N',
  require => File['/root/.ssh'],
}

