<p align="center">
  <img src="images/logo-small.png">
</p>

# This is the repository of the website at [krackattacks.com](https://www.krackattacks.com)

Feel free to submit pull requests to fix spellings mistakes or suggest new Q&A entries.

# Introduction
We discovered serious weaknesses in WPA2, a protocol that secures all modern protected Wi-Fi networks. An attacker within range of a victim can exploit these weaknesses using key reinstallation attacks (KRACKs). Concretely, attackers can use this novel attack technique to read information that was previously assumed to be safely encrypted.	This can be abused to steal sensitive information such as credit card numbers, passwords, chat messages, emails, photos, and so on. The attack works against all modern protected Wi-Fi networks. Depending on the network configuration, it is also possible to inject and manipulate data. For example, an attacker might be able to inject ransomware or other malware into websites.

The weaknesses are in the Wi-Fi standard itself, and not in individual products or implementations. Therefore, any correct implementation of WPA2 is likely affected. To prevent the attack, users must update affected products as soon as security updates become available. Note that if your device supports Wi-Fi, it is most likely affected. During our initial research, we discovered ourselves that Android, Linux, Apple, Windows, OpenBSD, MediaTek, Linksys, and others, are all affected by some variant of the attacks. For more information about specific products, consult the database of CERT/CC, or contact your vendor.

The research behind the attack will be presented at the Computer and Communications Security (CCS) conference, and at the Black Hat Europe conference. Our detailed research paper can already be downloaded.

# Demonstration
As a proof-of-concept we executed a key reinstallation attack against an Android smartphone. In this demonstration, the attacker is able to decrypt all data that the victim transmits. For an attacker this is easy to accomplish, because our key reinstallation attack is exceptionally devastating against Linux and Android 6.0 or higher. This is because Android and Linux can be tricked into (re)installing an all-zero encryption key (see below for more info). When attacking other devices, it is harder to decrypt all packets, although a large number of packets can nevertheless be decrypted. In any case, the following demonstration highlights the type of information that an attacker can obtain when performing key reinstallation attacks against protected Wi-Fi networks:

[KRACK Attacks: Bypassing WPA2 against Android and Linux](https://www.youtube.com/watch?v=Oh4WURZoR98)
