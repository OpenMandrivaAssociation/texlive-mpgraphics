%global tl_name mpgraphics
%global tl_revision 29776

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Process and display MetaPost figures inline
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mpgraphics
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mpgraphics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mpgraphics.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mpgraphics.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows LaTeX users to typeset MetaPost code inline and
display figures in their documents with only and only one run of LaTeX,
pdfLaTeX or XeLaTeX (no separate runs of mpost). Mpgraphics achieves
this by using the shell escape (\write 18) feature of current TeX
distributions, so that the whole process is automatic and the end user
is saved the tiresome processing.

