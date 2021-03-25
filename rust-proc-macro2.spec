# * RUSTC_BOOTSTRAP breaks tests
%bcond_with check
%global debug_package %{nil}

%global crate proc-macro2

Name:           rust-%{crate}
Version:        1.0.24
Release:        1
Summary:        Stable implementation of the upcoming new `proc_macro` API

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/proc-macro2
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Stable implementation of the upcoming new `proc_macro` API. Comes with an
option, off by default, to also reimplement itself in terms of the upstream
unstable API.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+proc-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proc-macro-devel %{_description}

This package contains library source intended for building other packages
which use "proc-macro" feature of "%{crate}" crate.

%files       -n %{name}+proc-macro-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+span-locations-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+span-locations-devel %{_description}

This package contains library source intended for building other packages
which use "span-locations" feature of "%{crate}" crate.

%files       -n %{name}+span-locations-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
