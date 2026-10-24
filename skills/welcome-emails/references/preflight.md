# Pre-send test list

Run this on the live automation with a test address, not on drafts in the editor. Previews in email tools don't show what Gmail, Outlook or Apple Mail will really do.

## Sending setup

- [ ] The sending domain has SPF, DKIM and a DMARC record. Most email tools have a page that shows the status.
- [ ] The from-name is the same in every email and is a name the subscriber will recognize.
- [ ] Replies go to an inbox someone reads.
- [ ] One-click unsubscribe is on, and the footer has a working unsubscribe link and a postal address.

## Each email

- [ ] Test sends reach Gmail, Outlook and Apple Mail. Check them on a phone and on a desktop.
- [ ] The email still makes sense with images turned off. Images need alt text, and no key message should live only inside an image.
- [ ] Every link was clicked from the test send, after tracking was added. Each lands on the right page, and that page does what the email said.
- [ ] Personalization works when the field is empty. "Hi ," is a bug, so set a fallback.
- [ ] The subject and preheader show correctly in the inbox list on a phone.
- [ ] Proofread the final version, after tracking links and merge fields are in.

## The automation

- [ ] A test subscriber who joins through the real form gets email 1 within a few minutes.
- [ ] The delays between emails are set as planned, and you've noted the time zone.
- [ ] A test subscriber tagged as a buyer leaves the offer emails.
- [ ] If there are branches, a test subscriber goes down each one.
- [ ] At the end of the sequence, subscribers join the regular newsletter and don't get the welcome sequence again.
- [ ] Someone owns the replies to "reply and tell me..." emails and will answer them.

Write down every defect you find, so the next sequence starts from a better list.
