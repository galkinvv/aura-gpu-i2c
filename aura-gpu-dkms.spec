%global debug_package %{nil}
%global dkms_name aura-gpu

Name:       %{dkms_name}-dkms
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    i2c driver for AURA capable GPUs 
License:    GPLv2
URL:        https://github.com/KyleGospo/aura-gpu-dkms
BuildArch:  noarch

Source:     {{{ git_dir_pack }}}

Provides:   %{dkms_name}-dkms = %{version}
Requires:   dkms

%description
i2c driver for AURA capable GPUs 

%prep
{{{ git_dir_setup_macro }}}

%build

%install
# Create empty tree
mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
cp -fr * %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

install -d %{buildroot}%{_sysconfdir}/modules-load.d
cat > %{buildroot}%{_sysconfdir}/modules-load.d/aura-gpu.conf << EOF
aura-gpu
EOF

%post -n %{name}
dkms add -m %{dkms_name} -v %{version} -q || :
# Rebuild and make available for the currently running kernel
dkms build -m %{dkms_name} -v %{version} -q || :
dkms install -m %{dkms_name} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{version} -q --all || :

%files
%license LICENSE
%doc README.md
%{_usrsrc}/%{dkms_name}-%{version}
%{_sysconfdir}/modules-load.d/aura-gpu.conf

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}