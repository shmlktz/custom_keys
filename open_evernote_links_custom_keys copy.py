##open links
import webbrowser

webbrowser.open('evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/')  


##########EVERNOTE IN APP URL STRUCTURE

# Structure

#      evernote:///view/[userId]/[shardId]/[noteGuid]/[noteGuid]/

# Where:

# [userId] is the user id of the notebook owner
# [shardId] is the shard id of the notebook owner
# [noteGuid] is the guid of the note that is being linked to
# Please note that the note GUID is listed at the end of the link twice, sequentially.

# Examples:

# evernote:///view/76136038/s12/4d971333-8b65-45d6-857b-243c850cabf5/4d971333-8b65-45d6-857b-243c850cabf5/2cd4dc67-1d52-401f-9aad-d5524b646ba2
#############################
#### TEST LINK to open in desktop: evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/
#############################
##usethis quickly draw data
##An actual link of mine: https://www.evernote.com/l/AMAQtCR7XwlLZpU9AuXyeqw8AzKRLSSSbA8
##: https://www.evernote.com/shard/s192/client/snv?noteGuid=10b4247b-5f09-4b66-953d-02e5f27aac3c&noteKey=0332912d24926c0f&sn=https%3A%2F%2Fwww.evernote.com%2Fshard%2Fs192%2Fsh%2F10b4247b-5f09-4b66-953d-02e5f27aac3c%2F0332912d24926c0f&title=love%2Bwhat%2Byou%2527re%2Bdoing%2B%2526%2B%2528why%252F%2529%2Bwhat%2Byou%2527re%2Bdoing%2Bit%2Bfor
#https://www.evernote.com/shard/s192/nl/21614375/10b4247b-5f09-4b66-953d-02e5f27aac3c/
#      https://[service]/shard/[shardId]/nl/[userId]/[noteGuid]/

# Where:

# [service] is the name of the Evernote service (either sandbox.evernote.com or www.evernote.com)
# [userId] is the user ID of the notebook owner
# [shardId] is the shard ID where the note is stored
# [noteGuid] is the GUID of the note that is being linked to
# Example:

# https://www.evernote.com/shard/s12/nl/76136038/d72dfad0-7d58-41b5-b2c9-4ca434abd543/