# Security

First, a disclaimer: in-depth security considerations, particularly as they pertain to web servers, are beyond the scope of this manual. Consult or become an expert!

Having said that, it’s worth making a distinction between using Linton to build a web site, and running the site:

+ Linton is designed to be simple to use to build a web site, and open: in particular, you can combine it with any other tool you like. This means that you should only use it with inputs and on a computer you trust.
+ However, the resulting web site is “just” a set of files, and in particular includes no components that must run on a web server. This means that Linton web sites are unlikely to pose particular security problems for the servers they run on, unless you add functionality well beyond the scope of the example web site produced by `linton init`.
+ Finally, web sites closely based on the Linton template are unlikely to pose security risks to their users: they should consist only of the input files, plus some well-known components such as the Bootstrap web framework, downloaded securely from well-known servers. However, producing sites safely requires that you have used Linton sensibly; see the first point above. If the computer you use to produce a site has been compromised, then it could easily contain malware or other security risks.