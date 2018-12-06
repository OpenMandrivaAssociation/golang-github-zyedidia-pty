# Run tests in check section
%bcond_without check

%global goipath         github.com/zyedidia/pty
%global commit          30364665a2445782b12bcb2db75f16ce684da907

%global common_description %{expand:
Pty is a Go package for using unix pseudo-terminals.}

%gometa

Name:    %{goname}
Version: 1.1.1
Release: 0.3%{?dist}
Summary: PTY interface for Go
License: MIT
URL:     %{gourl}
Source:  %{gosource}

%description
%{common_description}


%package    devel
Summary:    %{summary}
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license License
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-0.3.git3036466
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-0.2.20180314git3036466
- Update with the new Go packaging

* Fri Jan 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-0.1.20180126git3036466
- Initial package for Fedora

