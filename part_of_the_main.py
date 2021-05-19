from botCommand import check_string_in_reaction, id_reaction

@client.event
async def on_message(message):

    print(message.content)

    if message.author == client.user:
        print(message.author , ' | ' , client.user)
        return

    if (message.content.find('bot') != -1):
        # reaction trigger for check reaction

        check_id_reaction = [] #list for each reaction... 0,_,0
        id_max = 0
        array_message = message.content.split() #convert message into list

        for msg in array_message:
            answer_id = check_string_in_reaction(msg).
            #check each word in list message for trigger words

            if answer_id != None:
                check_id_reaction[answer_id] += 1
        
        for number in check_id_reaction:
            if id_max <= number:
                id_max = number
        
        if id_max == 0:
            await message.channel.send('What? I dont get it...')
        else:
            id_index = check_id_reaction.index(id_max)

            answer = id_reaction(id_index)
            
            await message.channel.send(answer)
