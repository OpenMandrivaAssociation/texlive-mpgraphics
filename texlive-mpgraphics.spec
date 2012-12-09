# revision 27230
# category Package
# catalog-ctan /macros/latex/contrib/mpgraphics
# catalog-date 2012-07-25 12:42:57 +0200
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-mpgraphics
Version:	0.3
Release:	1
Summary:	Process and display MetaPost figures inline
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mpgraphics
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpgraphics.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpgraphics.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpgraphics.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows LaTeX users to typeset MetaPost code inline
and display figures in their documents with only and only one
run of LaTeX, PDFLaTeX or XelaTeX (no separate runs of mpost).
Mpgraphics achieves this by using the shell escape (\write 18)
feature of current TeX distributions, so that the whole process
is automatic and the end user is saved the tiresome processing.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mpgraphics/mpgraphics.sty
%doc %{_texmfdistdir}/doc/latex/mpgraphics/README
%doc %{_texmfdistdir}/doc/latex/mpgraphics/mpgraphics-example.ltx
%doc %{_texmfdistdir}/doc/latex/mpgraphics/mpgraphics.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mpgraphics/mpgraphics.dtx
%doc %{_texmfdistdir}/source/latex/mpgraphics/mpgraphics.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 812632
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 754116
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719070
- texlive-mpgraphics
- texlive-mpgraphics
- texlive-mpgraphics
- texlive-mpgraphics

