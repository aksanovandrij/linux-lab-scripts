Name:           count-files
Version:        1.0
Release:        1%{?dist}
Summary:        Script to count regular files in /etc

License:        MIT
URL:            https://github.com/aksanovandrij/linux-lab-scripts
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash
Requires:       coreutils
Requires:       findutils

%description
A Bash script that counts the number of regular files
in the /etc directory, excluding directories and symbolic links.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 count_files.sh %{buildroot}%{_bindir}/count_files



%pre
s='count-files %{version} [pre]: installing'
set -- 31 33 32 36 34 35
while [ -n "$s" ]; do
  c=${s%%"${s#?}"}
  s=${s#?}
  printf "\033[1;${1}m${c}"
  k=$1; shift; set -- "$@" "$k"
done
printf '\033[0m\n'

%post
s='count-files %{version} [post]: script installed'
set -- 31 33 32 36 34 35
while [ -n "$s" ]; do
  c=${s%%"${s#?}"}
  s=${s#?}
  printf "\033[1;${1}m${c}"
  k=$1; shift; set -- "$@" "$k"
done
printf '\033[0m\n'

%preun
s='count-files %{version} [preun]: removing'
set -- 31 33 32 36 34 35
while [ -n "$s" ]; do
  c=${s%%"${s#?}"}
  s=${s#?}
  printf "\033[1;${1}m${c}"
  k=$1; shift; set -- "$@" "$k"
done
printf '\033[0m\n'

%postun
s='count-files %{version} [postun]: removed'
set -- 31 33 32 36 34 35
while [ -n "$s" ]; do
  c=${s%%"${s#?}"}
  s=${s#?}
  printf "\033[1;${1}m${c}"
  k=$1; shift; set -- "$@" "$k"
done
printf '\033[0m\n'



%files
%{_bindir}/count_files

%changelog
* Sun Nov 15 2026 Aksanov Andrij <aksanovandrij@gmail.com> - 1.0-1
- Initial package release
