用戶端ID： 336d7f7yvbajkj2spzyk0z6wu32pz3
密碼： zct3yys5sr3airgmgx98c4mc629g4z

獲取token指令：
curl -X POST "https://id.twitch.tv/oauth2/token" -H "Content-Type: application/x-www-form-urlencoded" -d "client_id=336d7f7yvbajkj2spzyk0z6wu32pz3&client_secret=zct3yys5sr3airgmgx98c4mc629g4z&grant_type=client_credentials"

token：
{
    "access_token":"fnei9cskh8rbbtisei6ewj17yomm4o",
    "expires_in":4701598,
    "token_type":"bearer"
}

Make your first call：
curl -X GET "https://api.twitch.tv/helix/users?login=twitchdev" -H "Authorization: Bearer fnei9cskh8rbbtisei6ewj17yomm4o" -H "Client-Id: 336d7f7yvbajkj2spzyk0z6wu32pz3"

Back：
{"data":[{"id":"141981764","login":"twitchdev","display_name":"TwitchDev","type":"","broadcaster_type":"partner","description":"Supporting third-party developers building Twitch integrations from chatbots to game integrations.","profile_image_url":"https://static-cdn.jtvnw.net/jtv_user_pictures/8a6381c7-d0c0-4576-b179-38bd5ce1d6af-profile_image-300x300.png","offline_image_url":"https://static-cdn.jtvnw.net/jtv_user_pictures/3f13ab61-ec78-4fe6-8481-8682cb3b0ac2-channel_offline_image-1920x1080.png","view_count":19044088,"created_at":"2016-12-14T20:32:28Z"}]}

安裝scoop，安裝Twitch CLI
設定Twitch CLI：
twitch configure -i 336d7f7yvbajkj2spzyk0z6wu32pz3 -s zct3yys5sr3airgmgx98c4mc629g4z


