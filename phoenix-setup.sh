# Run in code repo after it has been copied onto the VM

yes | mix do deps.get, compile, ecto.create, ecto.migrate, phx.server
