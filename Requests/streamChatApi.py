import stream_chat

server_client = stream_chat.StreamChat(api_key="ah48ckptkjvm",
       api_secret="gfcfa94ghkctn3du36s2d4nmqg9q24wtxhr56qd84pj7dum94ahhtedccj8q7wk4")

token = server_client.create_token('john')
# john - eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiam9obiJ9.9-vTGOl-FWxdSpt-hgFiRSyRcl4_2DDHNcNwGHKa2KA
# tom - eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidG9tIn0._HkDWmGM3ItRXTLn9-s7N_8XBew_DxHBBH9eDHjRtP4
print(token)